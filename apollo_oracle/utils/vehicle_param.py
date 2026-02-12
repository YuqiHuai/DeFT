from dataclasses import dataclass

from google.protobuf import text_format

from apollo_modules.modules.common.configs.proto.vehicle_config_pb2 import VehicleConfig


@dataclass(slots=True)
class VehicleParam:
    length: float
    width: float
    height: float
    front2center: float
    back2center: float
    left2center: float
    right2center: float

    @staticmethod
    def load_from_file(filename: str):
        with open(filename, 'r') as fp:
            msg = text_format.Parse(fp.read(), VehicleConfig())
            apollo_vehicle_param = msg.vehicle_param
            vp = VehicleParam(
                length=apollo_vehicle_param.length,
                width=apollo_vehicle_param.width,
                height=apollo_vehicle_param.height,
                front2center=apollo_vehicle_param.front_edge_to_center,
                back2center=apollo_vehicle_param.back_edge_to_center,
                left2center=apollo_vehicle_param.left_edge_to_center,
                right2center=apollo_vehicle_param.right_edge_to_center,
            )
            return vp
