# 10 subscriptions
import json
import pathlib
from dataclasses import dataclass
from typing import Optional

from autoware_auto_mapping_msgs.msg import HADMapBin
from autoware_auto_perception_msgs.msg import PredictedObjects, TrafficSignalArray
from autoware_auto_planning_msgs.msg import (
    Path,
    PathWithLaneId,
)

# ruff: noqa: F401
from diagnostic_msgs.msg import DiagnosticStatus
from geometry_msgs.msg import AccelWithCovarianceStamped
from loguru import logger
from nav_msgs.msg import OccupancyGrid, Odometry
from rclpy.serialization import deserialize_message, serialize_message
from sensor_msgs.msg import PointCloud2
from tf2_msgs.msg import TFMessage
from tier4_planning_msgs.msg import VelocityLimit
from tier4_v2x_msgs.msg import VirtualTrafficLightStateArray

# ruff: noqa: F401
from visualization_msgs.msg import MarkerArray

from deft_autoware.utils import msg_to_dict


@dataclass
class AutowareUnitTestInputs:
    tf: TFMessage
    path_with_lane_id: PathWithLaneId
    predicted_objects: PredictedObjects
    point_cloud2: PointCloud2
    odometry: Odometry
    accel_with_covariance_stamped: AccelWithCovarianceStamped
    had_map_bin: HADMapBin
    occupancy_grid: OccupancyGrid

    traffic_signal_array: Optional[TrafficSignalArray] = None
    velocity_limit: Optional[VelocityLimit] = None
    virtual_traffic_light_state_array: Optional[VirtualTrafficLightStateArray] = None

    def to_dict(self):
        result = {
            'path_with_lane_id': msg_to_dict(self.path_with_lane_id),
            'predicted_objects': msg_to_dict(self.predicted_objects),
            'point_cloud2': msg_to_dict(self.point_cloud2),
            'odometry': msg_to_dict(self.odometry),
            'accel_with_covariance_stamped': msg_to_dict(
                self.accel_with_covariance_stamped
            ),
            'had_map_bin': msg_to_dict(self.had_map_bin),
            'occupancy_grid': msg_to_dict(self.occupancy_grid),
        }
        if self.traffic_signal_array is not None:
            result['traffic_signal_array'] = msg_to_dict(self.traffic_signal_array)
        if self.velocity_limit is not None:
            result['velocity_limit'] = msg_to_dict(self.velocity_limit)
        if self.virtual_traffic_light_state_array is not None:
            result['virtual_traffic_light_state_array'] = msg_to_dict(
                self.virtual_traffic_light_state_array
            )
        return result

    @staticmethod
    def get_stub():
        return AutowareUnitTestInputs(
            TFMessage(),
            PathWithLaneId(),
            PredictedObjects(),
            PointCloud2(),
            Odometry(),
            AccelWithCovarianceStamped(),
            HADMapBin(),
            OccupancyGrid(),
            TrafficSignalArray(),
            VelocityLimit(),
            VirtualTrafficLightStateArray(),
        )


@dataclass
class AutowareUnitTestOutput:
    path: Path

    def to_dict(self):
        return {
            'path': msg_to_dict(self.path),
        }

    @staticmethod
    def get_stub():
        return AutowareUnitTestOutput(Path())


@dataclass
class AutowareUnitTestFrame:
    inputs: AutowareUnitTestInputs
    outputs: AutowareUnitTestOutput

    @staticmethod
    def get_stub():
        return AutowareUnitTestFrame(
            AutowareUnitTestInputs.get_stub(),
            AutowareUnitTestOutput.get_stub(),
        )


def write_frame_to_directory(
    frame: AutowareUnitTestFrame, directory: str, write_json: bool = False
):
    out_dir = pathlib.Path(directory)
    out_inputs = pathlib.Path(out_dir, 'inputs')
    out_outputs = pathlib.Path(out_dir, 'outputs')

    out_dir.mkdir(parents=True, exist_ok=True)
    out_inputs.mkdir(parents=True, exist_ok=True)
    out_outputs.mkdir(parents=True, exist_ok=True)

    if write_json:
        with open(pathlib.Path(out_dir, '_inputs.json'), 'w') as f:
            f.write(json.dumps(frame.inputs.to_dict(), indent=4))

        with open(pathlib.Path(out_dir, '_outputs.json'), 'w') as f:
            f.write(json.dumps(frame.outputs.to_dict(), indent=4))

    # write serialized inputs
    for key in frame.inputs.__dict__.keys():
        value = frame.inputs.__getattribute__(key)
        if value is not None:
            binary_file_path = pathlib.Path(out_dir, 'inputs', f'{key}.bin')
            with open(binary_file_path, 'wb') as f:
                f.write(serialize_message(value))

    # write serialized output
    for key in frame.outputs.__dict__.keys():
        value = frame.outputs.__getattribute__(key)
        if value is not None:
            binary_file_path = pathlib.Path(out_dir, 'outputs', f'{key}.bin')
            with open(binary_file_path, 'wb') as f:
                f.write(serialize_message(value))

    logger.info(f'Written inputs to {out_dir.absolute()}')


def load_frame_from_directory(directory: str) -> AutowareUnitTestFrame:
    in_dir = pathlib.Path(directory)
    in_inputs = pathlib.Path(in_dir, 'inputs')
    in_outputs = pathlib.Path(in_dir, 'outputs')

    inputs = AutowareUnitTestInputs.get_stub()
    outputs = AutowareUnitTestOutput.get_stub()

    # load serialized inputs
    for key in inputs.__dict__.keys():
        binary_file_path = pathlib.Path(in_inputs, f'{key}.bin')
        if binary_file_path.exists():
            with open(binary_file_path, 'rb') as f:
                # get type of message
                message_type = inputs.__getattribute__(key).__class__
                inputs.__setattr__(key, deserialize_message(f.read(), message_type))

    # load serialized outputs
    for key in outputs.__dict__.keys():
        binary_file_path = pathlib.Path(in_outputs, f'{key}.bin')
        if binary_file_path.exists():
            with open(binary_file_path, 'rb') as f:
                # get type of message
                message_type = outputs.__getattribute__(key).__class__
                outputs.__setattr__(key, deserialize_message(f.read(), message_type))

    return AutowareUnitTestFrame(inputs, outputs)
