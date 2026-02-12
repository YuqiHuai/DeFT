from typing import Dict, Optional

import numpy as np
from shapely import Polygon
from shapely.geometry import Point

from apollo_oracle.core import OracleExtension, Violation
from apollo_oracle.utils import generate_adc_polygon
from apollo_oracle.utils.map_service import MapService
from apollo_oracle.utils.vehicle_param import VehicleParam


class DestinationOracle(OracleExtension):
    DESTINATION_THRESHOLD = 5.0

    @staticmethod
    def get_name():
        return 'destination'

    def __init__(
        self, map_service: MapService, vehicle_param: VehicleParam, args_dict: Dict
    ):
        super().__init__(map_service, vehicle_param, args_dict)
        self.destination: Optional[Point] = None
        self.last_position: Optional[Polygon] = None

    def get_interested_topics(self):
        return ['/apollo/localization/pose', '/apollo/routing_request']

    def on_message(self, topic, msg, t):
        if topic == '/apollo/routing_request':
            if self.destination is not None:
                return
            destination = msg.waypoint[-1]

            if np.isnan(destination.pose.x) or np.isnan(destination.pose.y):
                lane_id = destination.id
                s = destination.s
                coord, _ = self.map_service.get_lane_coord_and_heading(lane_id, s)
                self.destination = coord
            else:
                self.destination = Point(destination.pose.x, destination.pose.y)
        elif topic == '/apollo/localization/pose':
            self.last_position = Polygon(
                generate_adc_polygon(
                    msg.pose.position.x,
                    msg.pose.position.y,
                    msg.pose.position.z,
                    msg.pose.heading,
                    self.vehicle_param,
                )
            )

    def get_violations(self):
        if self.destination is None or self.last_position is None:
            return []
        return [
            Violation(
                self.get_name(),
                self.destination.distance(self.last_position)
                >= self.DESTINATION_THRESHOLD,
                {'dist2destination': self.destination.distance(self.last_position)},
            )
        ]
