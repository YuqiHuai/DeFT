from pathlib import Path
from typing import Any, Dict, Tuple

import numpy as np
from cyber_record.record import Record
from scipy import interpolate
from shapely import LineString, Polygon

from apollo_oracle.core import OracleExtension, Violation
from apollo_oracle.utils import (
    generate_adc_polygon,
    generate_polygon,
)
from apollo_oracle.utils.map_service import MapService
from apollo_oracle.utils.obstacle import APOLLO_OBSTACLE_TYPE, Obstacle
from apollo_oracle.utils.vehicle_param import VehicleParam


class OptimalOracle(OracleExtension):
    OPTIMAL_THRESHOLD = 0.4
    GRID_UNIT = 2.0

    @staticmethod
    def get_name():
        return 'optimal'

    @staticmethod
    def register_arguments(parser):
        parser.add_argument(
            '--optimal_refer',
            type=str,
            nargs=1,
            required=False,
            help='Specify reference record file for optimal oracle',
        )

    def __init__(
        self, map_service: MapService, vehicle_param: VehicleParam, args_dict: Dict
    ):
        super().__init__(map_service, vehicle_param, args_dict)
        self.refer_record_path = args_dict.get('optimal_refer')[0]
        assert Path(self.refer_record_path).exists()

        self.start_t = None
        self.ego_trace_pts = []
        self.obstacle_frames = []

    def get_interested_topics(self):
        return [
            '/apollo/perception/obstacles',
            '/apollo/localization/pose',
            '/apollo/routing_request',
            '/apollo/routing_response',
        ]

    def on_message(self, topic, msg, t):
        # if topic == '/apollo/routing_request':
        #     print(msg)

        if topic == '/apollo/routing_request':
            self.start_t = t
            pass
        elif topic == '/apollo/localization/pose':
            ego_x = msg.pose.position.x
            ego_y = msg.pose.position.y
            self.ego_trace_pts.append((ego_x, ego_y))
            # self.ego_frames.append((t, ego_x, ego_y, msg.pose.heading))
            pass
        elif topic == '/apollo/perception/obstacles':
            obstacle_frame = dict()
            for obs in msg.perception_obstacle:
                obj = Obstacle(
                    id=obs.id,
                    type=APOLLO_OBSTACLE_TYPE[obs.type],
                    position=(obs.position.x, obs.position.y, obs.position.z),
                    velocity=(obs.velocity.x, obs.velocity.y, obs.velocity.z),
                    length=obs.length,
                    width=obs.width,
                    height=obs.height,
                    theta=obs.theta,
                )
                obstacle_frame[obj.id] = obj
            timestamp = float(np.clip((t - self.start_t) * 1e-9, 0.0, None))
            self.obstacle_frames.append((timestamp, obstacle_frame))
        pass

    def get_violations(self):
        self._preprocess()
        # 1. check original can pass
        is_replay_pass = self._is_replay_pass()  # true: pass, false: not pass
        # 2. check path optimal
        is_non_optimal, diff_iou_value, lane_id = (
            self._is_non_optimal()
        )  # true: non-optimal, false: optimal

        # oracle = [
        #     is_replay_pass,
        #     is_non_optimal,
        #     diff_iou_value,
        #     lane_id,
        # ]  # [True, True] is violation
        return [
            Violation(
                name=self.get_name(),
                triggered=is_replay_pass and is_non_optimal,
                features={'diff_iou_value': diff_iou_value, 'lane_id': lane_id},
            )
        ]

    def _preprocess(self):  # noqa: C901
        refer_record = Record(self.refer_record_path)

        refer_ego_lanes = []
        refer_lane_occupancy = dict()
        # find refer grid
        # 1. extract trace lanes
        for topic, msg, t in refer_record.read_messages(['/apollo/routing_response']):
            for road in msg.road:
                for passage in road.passage:
                    refer_ego_lanes.append(passage.segment[0].id)
            break
        assert len(refer_ego_lanes) > 0

        # 2. split refer lanes with trace
        refer_lane_grid = dict()
        for lane_id in refer_ego_lanes:  # change to only ego lanes
            # for trace difference
            refer_lane_grid[lane_id] = list()
            lane_left_boundary, lane_right_boundary = (
                self.map_service.get_lane_boundary_curve(lane_id)
            )
            lane_line_length = self.map_service.get_length_of_lane(lane_id)
            num_points = int(lane_line_length / self.GRID_UNIT) + 1
            num_points = max(num_points, 2)
            left_sample_points = [
                lane_left_boundary.interpolate(
                    i / float(num_points - 1), normalized=True
                )
                for i in range(num_points)
            ]
            right_sample_points = [
                lane_right_boundary.interpolate(
                    i / float(num_points - 1), normalized=True
                )
                for i in range(num_points)
            ]

            assert len(left_sample_points) == len(right_sample_points)

            for i in range(len(left_sample_points)):
                refer_lane_grid[lane_id].append(
                    LineString([left_sample_points[i], right_sample_points[i]])
                )
        self.refer_lane_grid = refer_lane_grid

        # 3. calculate grids for refer ego
        ego_frames = []
        start_t = None
        for _, msg, t in refer_record.read_messages('/apollo/localization/pose'):
            if start_t is None:
                start_t = t
            relative_time = float(np.clip((t - start_t) * 1e-9, 0.0, None))
            ego_frames.append(
                (
                    relative_time,
                    msg.pose.position.x,
                    msg.pose.position.y,
                    msg.pose.heading,
                )
            )

        ego_trace_pts = [(x[1], x[2]) for x in ego_frames]
        refer_ego_trace: LineString = LineString(ego_trace_pts)
        refer_lane_occupancy = dict()
        for lane_id, line_lst in refer_lane_grid.items():
            lane_grid_num = len(line_lst)
            # if lane_grid_num < 2:
            #     continue
            lane_grid_nonzero_count = 0
            lane_occupancy = np.zeros(lane_grid_num)
            for line_index in range(lane_grid_num):
                seg_line = line_lst[line_index]
                if refer_ego_trace.intersects(seg_line):
                    lane_occupancy[line_index] = 1
                    lane_grid_nonzero_count += 1
            lane_nonzero_rate = lane_grid_nonzero_count / float(lane_grid_num)
            if lane_nonzero_rate < 0.05:
                continue
            refer_lane_occupancy[lane_id] = lane_occupancy

        self.refer_lane_occupancy = refer_lane_occupancy

        # 4. calculate fx
        refer_ts = list()
        refer_xs = list()
        refer_ys = list()
        refer_headings = list()

        for frame in ego_frames:
            refer_ts.append(frame[0])
            refer_xs.append(frame[1])
            refer_ys.append(frame[2])
            refer_headings.append(frame[3])

        self.f_x = interpolate.interp1d(refer_ts, np.array(refer_xs), kind='linear')
        self.f_y = interpolate.interp1d(refer_ts, np.array(refer_ys), kind='linear')
        self.f_heading = interpolate.interp1d(
            refer_ts, np.array(refer_headings), kind='linear'
        )
        self.refer_t = refer_ts[-1]

    def _is_replay_pass(self) -> bool:
        """
        replay reference ego behaviors in current record
        """
        for frame_time, obstacles in self.obstacle_frames:
            # ignore self.refer_t > last_current_time
            if frame_time >= self.refer_t:
                break
            ##### extract prev ego polygon in curr env #####
            refer_ego_x = float(self.f_x(frame_time))
            refer_ego_y = float(self.f_y(frame_time))
            refer_ego_heading = float(self.f_heading(frame_time))
            refer_ego_polygon = Polygon(
                generate_adc_polygon(
                    refer_ego_x, refer_ego_y, 0.0, refer_ego_heading, self.vehicle_param
                )
            )
            ##### End this part #####

            for obs_id, obs in obstacles.items():
                obs_polygon = Polygon(
                    generate_polygon(
                        pos_x=obs.position[0],
                        pos_y=obs.position[1],
                        pos_z=obs.position[2],
                        theta=obs.theta,
                        length=obs.length,
                        width=obs.width,
                    )
                )
                if refer_ego_polygon.distance(obs_polygon) <= 0.0:
                    return False
        return True

    def _is_non_optimal(self) -> Tuple[bool, float, Any]:
        # calculate the occupancy for record
        ego_trace: LineString = LineString(self.ego_trace_pts)
        # trace_length_diff = ego_trace.length - self.refer_record.ego_trace.length

        ego_occupancy = dict()
        grid_diff_iou = dict()
        refer_lane_grid = self.refer_lane_grid
        refer_occupancy = self.refer_lane_occupancy
        max_lane_diff_iou = 0.0
        max_lane_id = ''
        for lane_id in refer_occupancy.keys():
            line_lst = refer_lane_grid[lane_id]
            ego_occupancy[lane_id] = np.zeros(len(line_lst))
            for line_index in range(len(line_lst)):
                seg_line = line_lst[line_index]
                if ego_trace.intersects(seg_line):
                    ego_occupancy[lane_id][line_index] = 1

            diff = np.linalg.norm(
                refer_occupancy[lane_id] - ego_occupancy[lane_id], ord=1
            )
            union = np.where(
                (refer_occupancy[lane_id] + ego_occupancy[lane_id]) > 0, 1, 0
            )
            grid_diff_iou[lane_id] = float(diff / float(np.sum(union) + 1e-5))
            if grid_diff_iou[lane_id] > max_lane_diff_iou:
                max_lane_diff_iou = grid_diff_iou[lane_id]
                max_lane_id = lane_id

        if max_lane_diff_iou > self.OPTIMAL_THRESHOLD:
            return True, max_lane_diff_iou, max_lane_id
        else:
            return False, max_lane_diff_iou, max_lane_id
