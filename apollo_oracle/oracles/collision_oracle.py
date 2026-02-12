from collections import defaultdict
from typing import Dict, List, Optional, Set, Tuple

from shapely import LineString
from shapely.geometry import Polygon

from apollo_oracle.core import OracleExtension, OracleInterrupt, Violation
from apollo_oracle.utils import (
    generate_adc_front_vertices,
    generate_adc_polygon,
    generate_adc_rear_vertices,
    generate_polygon,
)
from apollo_oracle.utils.map_service import MapService
from apollo_oracle.utils.obstacle import APOLLO_OBSTACLE_TYPE, Obstacle
from apollo_oracle.utils.vehicle_param import VehicleParam


class CollisionOracle(OracleExtension):
    COLLISION_THRESHOLD = 1e-3

    @staticmethod
    def get_name():
        return 'collision'

    def __init__(
        self, map_service: MapService, vehicle_param: VehicleParam, args_dict: Dict
    ):
        super().__init__(map_service, vehicle_param, args_dict)
        self.ignored_obstacles: Set[int] = set()
        self.obstacle_fitness: Dict[int, float] = defaultdict(lambda: float('inf'))
        self.last_localization: Optional[Tuple[Polygon, float]] = None
        self.last_perception_obstacles: Dict[int, Obstacle] = dict()
        self.violations: List[Violation] = list()

    def get_interested_topics(self):
        return [
            '/apollo/perception/obstacles',
            '/apollo/localization/pose',
        ]

    def on_message(self, topic, msg, t):
        if topic == '/apollo/perception/obstacles':
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
                self.last_perception_obstacles[obj.id] = obj
        if topic == '/apollo/localization/pose':
            ego_x = msg.pose.position.x
            ego_y = msg.pose.position.y
            ego_vx = msg.pose.linear_velocity.x
            ego_vy = msg.pose.linear_velocity.y
            ego_speed = (ego_vx**2 + ego_vy**2) ** 0.5
            ego_theta = msg.pose.heading
            ego_polygon = generate_adc_polygon(
                ego_x, ego_y, 0.0, ego_theta, self.vehicle_param
            )
            ego_p = Polygon(ego_polygon)
            ego_front = generate_adc_front_vertices(
                ego_x, ego_y, 0.0, ego_theta, self.vehicle_param
            )
            ego_front_l = LineString(ego_front)
            ego_rear = generate_adc_rear_vertices(
                ego_x, ego_y, 0.0, ego_theta, self.vehicle_param
            )
            ego_rear_l = LineString(ego_rear)

            for obs_id, obs in self.last_perception_obstacles.items():
                if obs_id in self.ignored_obstacles:
                    continue
                obs_p = Polygon(
                    generate_polygon(
                        pos_x=obs.position[0],
                        pos_y=obs.position[1],
                        pos_z=obs.position[2],
                        theta=obs.theta,
                        length=obs.length,
                        width=obs.width,
                    )
                )
                obs_distance = obs_p.distance(ego_p)
                self.obstacle_fitness[obs_id] = min(
                    self.obstacle_fitness[obs_id], obs_distance
                )
                if obs_distance < self.COLLISION_THRESHOLD:
                    if obs_p.distance(ego_front_l) < self.COLLISION_THRESHOLD:
                        # ego colliding into another obstacle
                        collision_type = 'front'
                    elif obs_p.distance(ego_rear_l) < self.COLLISION_THRESHOLD:
                        # ego being rear ended
                        collision_type = 'rear'
                    else:
                        # other collision
                        collision_type = 'side'
                    self.violations.append(
                        Violation(
                            self.get_name(),
                            True,
                            {
                                'ego_x': ego_x,
                                'ego_y': ego_y,
                                'ego_theta': ego_theta,
                                'ego_speed': ego_speed,
                                'obs_x': obs.position[0],
                                'obs_y': obs.position[1],
                                'obs_type': obs.type,
                                'obs_theta': obs.theta,
                                'obs_length': obs.length,
                                'obs_width': obs.width,
                                'collision_type': collision_type,
                            },
                        )
                    )
                    raise OracleInterrupt
                else:
                    # no collision
                    pass

    def get_violations(self):
        if len(self.violations) == 0:
            return [
                Violation(
                    name=self.get_name(),
                    triggered=False,
                    features={'min_dist': min(self.obstacle_fitness.values())},
                )
            ]
        return self.violations
