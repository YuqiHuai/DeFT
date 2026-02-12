from typing import Dict

import numpy as np

from apollo_oracle.core import OracleExtension, Violation
from apollo_oracle.utils.map_service import MapService
from apollo_oracle.utils.vehicle_param import VehicleParam


class AccelerationOracle(OracleExtension):
    FAST_ACCELERATION_THRESHOLD = 4.0
    HARD_BRAKING_THRESHOLD = -4.0

    @staticmethod
    def get_name():
        return 'acceleration'

    def __init__(
        self, map_service: MapService, vehicle_param: VehicleParam, args_dict: Dict
    ):
        super().__init__(map_service, vehicle_param, args_dict)
        self.max_acceleration = 0.0
        self.min_acceleration = 0.0

    def get_interested_topics(self):
        return [
            '/apollo/localization/pose',
        ]

    def on_message(self, topic, msg, t):
        vx = msg.pose.linear_velocity.x
        vy = msg.pose.linear_velocity.y
        ax = msg.pose.linear_acceleration.x
        ay = msg.pose.linear_acceleration.y
        acceleration = float(np.sqrt(np.square(ax) + np.square(ay)))

        projection = vx * ax + vy * ay
        if projection < 0:
            acceleration = -1 * acceleration

        self.max_acceleration = max(acceleration, self.max_acceleration)
        self.min_acceleration = min(acceleration, self.min_acceleration)

    def get_violations(self):
        triggered = (
            self.max_acceleration > self.FAST_ACCELERATION_THRESHOLD
            or self.min_acceleration < self.HARD_BRAKING_THRESHOLD
        )
        return [
            Violation(
                name=self.get_name(),
                triggered=triggered,
                features={
                    'max_acceleration': self.max_acceleration,
                    'min_acceleration': self.min_acceleration,
                },
            )
        ]
