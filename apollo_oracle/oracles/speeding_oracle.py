from typing import Dict

import numpy as np
from shapely import Point

from apollo_oracle.core import OracleExtension, Violation
from apollo_oracle.utils.map_service import MapService
from apollo_oracle.utils.vehicle_param import VehicleParam


class SpeedingOracle(OracleExtension):
    SPEEDING_THRESHOLD = 0.5  # meters per second

    @staticmethod
    def get_name():
        return 'speeding'

    def __init__(
        self, map_service: MapService, vehicle_param: VehicleParam, args_dict: Dict
    ):
        super().__init__(map_service, vehicle_param, args_dict)
        self.violations = []
        self.speed_over_limit = float('-inf')
        self.speed_over_limit_loc = None
        self.violated_lanes = set()

    def get_interested_topics(self):
        return [
            '/apollo/localization/pose',
        ]

    def on_message(self, topic, msg, t):
        x = msg.pose.position.x
        y = msg.pose.position.y
        heading = msg.pose.heading

        vx = msg.pose.linear_velocity.x
        vy = msg.pose.linear_velocity.y
        speed = np.sqrt(np.square(vx) + np.square(vy))

        lanes = self.map_service.get_nearest_lanes_with_heading(Point(x, y), heading)

        lanes = [lane for lane in lanes if lane not in self.violated_lanes]

        if len(lanes) == 0:
            return

        limits = [self.map_service.get_lane_by_id(x).speed_limit for x in lanes]

        if all((speed - limit) > self.SPEEDING_THRESHOLD for limit in limits):
            # violation happened
            self.violations.append(
                Violation(
                    self.get_name(),
                    triggered=True,
                    features={'speeding': speed - max(limits), 'ego_x': x, 'ego_y': y},
                )
            )
            for lane in lanes:
                self.violated_lanes.add(lane)

        if self.speed_over_limit < speed - max(limits):
            self.speed_over_limit = speed - max(limits)
            self.speed_over_limit_loc = x, y

    def get_violations(self):
        if len(self.violations) == 0:
            return [
                Violation(
                    self.get_name(),
                    triggered=False,
                    features={
                        'speeding': float(self.speed_over_limit),
                        'ego_x': self.speed_over_limit_loc[0],
                        'ego_y': self.speed_over_limit_loc[1],
                    },
                )
            ]
        return self.violations
