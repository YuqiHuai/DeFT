import pathlib
import threading
import time
from typing import List

import rclpy
import rclpy.qos
from autoware_auto_mapping_msgs.msg import HADMapBin
from autoware_auto_perception_msgs.msg import PredictedObjects, TrafficSignalArray
from autoware_auto_planning_msgs.msg import (
    Path,
    PathWithLaneId,
)
from autoware_record.record import Record
from builtin_interfaces.msg import Time

# ruff: noqa: F401
from diagnostic_msgs.msg import DiagnosticStatus
from geometry_msgs.msg import AccelWithCovarianceStamped
from loguru import logger
from nav_msgs.msg import OccupancyGrid, Odometry
from rclpy.context import Context
from rclpy.executors import MultiThreadedExecutor
from rclpy.node import Node
from rclpy.qos import QoSDurabilityPolicy, QoSProfile
from rclpy.serialization import deserialize_message, serialize_message
from ros2_easy_test import ROS2TestEnvironment, with_single_node
from rosgraph_msgs.msg import Clock
from sensor_msgs.msg import PointCloud2
from tf2_msgs.msg import TFMessage
from tier4_planning_msgs.msg import VelocityLimit
from tier4_v2x_msgs.msg import VirtualTrafficLightStateArray

# ruff: noqa: F401
from visualization_msgs.msg import MarkerArray

from deft_autoware.frame import AutowareUnitTestFrame, load_frame_from_directory
from deft_autoware.utils import get_topic_for_type

TOPIC_PREFIX = '/planning/scenario_planning/lane_driving/behavior_planning'
TOPIC_PREFIX = '/deft'


class TestPublisherNode(Node):
    def __init__(self, frame: AutowareUnitTestFrame, tfs: List[TFMessage]):
        super().__init__('deft_test_publisher_node')

        self.reset_time_publisher = self.create_publisher(Clock, '/reset_time', 10)

        self.clock_publisher = self.create_publisher(Clock, '/clock', 10)
        self.tf_publisher = self.create_publisher(TFMessage, '/tf', 10)
        self.path_with_lane_id_publisher = self.create_publisher(
            PathWithLaneId, f'{TOPIC_PREFIX}/path_with_lane_id', 10
        )
        self.predicted_objects_publisher = self.create_publisher(
            PredictedObjects, '/perception/object_recognition/objects', 10
        )
        self.point_cloud2_publisher = self.create_publisher(
            PointCloud2, '/perception/obstacle_segmentation/pointcloud', 10
        )
        self.odometry_publisher = self.create_publisher(
            Odometry, '/localization/kinematic_state', 10
        )
        self.accel_with_covariance_stamped_publisher = self.create_publisher(
            AccelWithCovarianceStamped, '/localization/acceleration', 10
        )
        self.had_map_bin_publisher = self.create_publisher(
            HADMapBin,
            '/map/vector_map',
            qos_profile=QoSProfile(
                depth=10, durability=QoSDurabilityPolicy.TRANSIENT_LOCAL
            ),
        )
        self.occupancy_grid_publisher = self.create_publisher(
            OccupancyGrid, '/perception/occupancy_grid_map/map', 10
        )
        self.traffic_signal_array_publisher = self.create_publisher(
            TrafficSignalArray,
            '/perception/traffic_light_recognition/traffic_signals',
            10,
        )
        self.velocity_limit_publisher = self.create_publisher(
            VelocityLimit,
            '/planning/scenario_planning/max_velocity_default',
            qos_profile=QoSProfile(
                depth=1, durability=QoSDurabilityPolicy.TRANSIENT_LOCAL
            ),
        )
        self.virtual_traffic_light_state_array_publisher = self.create_publisher(
            VirtualTrafficLightStateArray,
            '/perception/virtual_traffic_light_states',
            10,
        )

        clock = Clock()

        # publish reset time
        self.reset_time_publisher.publish(clock)

        # publish tf messages
        for tf in tfs:
            clock.clock = tf.transforms[0].header.stamp
            self.clock_publisher.publish(clock)
            self.tf_publisher.publish(tf)

        # publish all input messages
        if frame.inputs.tf:
            # frame.inputs.tf.transforms[0].header.stamp = frame.inputs.point_cloud2.header.stamp
            clock.clock = frame.inputs.tf.transforms[0].header.stamp
            self.clock_publisher.publish(clock)
            self.tf_publisher.publish(frame.inputs.tf)
        if frame.inputs.predicted_objects:
            self.predicted_objects_publisher.publish(frame.inputs.predicted_objects)
        if frame.inputs.point_cloud2:
            self.point_cloud2_publisher.publish(frame.inputs.point_cloud2)
        if frame.inputs.odometry:
            self.odometry_publisher.publish(frame.inputs.odometry)
        if frame.inputs.accel_with_covariance_stamped:
            self.accel_with_covariance_stamped_publisher.publish(
                frame.inputs.accel_with_covariance_stamped
            )
        if frame.inputs.had_map_bin:
            self.had_map_bin_publisher.publish(frame.inputs.had_map_bin)
        if frame.inputs.occupancy_grid:
            self.occupancy_grid_publisher.publish(frame.inputs.occupancy_grid)
        if frame.inputs.traffic_signal_array:
            self.traffic_signal_array_publisher.publish(
                frame.inputs.traffic_signal_array
            )
        if frame.inputs.velocity_limit:
            self.velocity_limit_publisher.publish(frame.inputs.velocity_limit)
        if frame.inputs.virtual_traffic_light_state_array:
            self.virtual_traffic_light_state_array_publisher.publish(
                frame.inputs.virtual_traffic_light_state_array
            )

        # synchronize clock
        clock = Clock()
        clock.clock = frame.outputs.path.header.stamp
        self.clock_publisher.publish(clock)

        # publish trigger
        if frame.inputs.path_with_lane_id:
            self.path_with_lane_id_publisher.publish(frame.inputs.path_with_lane_id)
            logger.info(
                f'Trigger published on {self.path_with_lane_id_publisher.topic}'
            )


class TestSubscriberNode(Node):
    def __init__(self, target_output_location: pathlib.Path):
        super().__init__('deft_test_subscriber_node')
        self.path_subscriber = self.create_subscription(
            Path, f'{TOPIC_PREFIX}/path', self.onPath, 10
        )
        self.target_output_location = target_output_location

    def onPath(self, msg):
        with open(self.target_output_location, 'wb') as f:
            f.write(serialize_message(msg))


def run_test_cases(
    test_record_directory: pathlib.Path,
    test_frames_directory: pathlib.Path,
    test_case_time_out: int = 5,
    maximum_retry: int = 3,
):
    assert (
        test_frames_directory.exists()
    ), f'Test frames directory {test_frames_directory} does not exist'
    assert (
        test_record_directory.exists()
    ), f'Test record directory {test_record_directory} does not exist'

    # load all tf messages
    tfs = []
    for _, msg, _ in Record(test_record_directory).read_messages(topic_name='/tf'):
        tfs.append(msg)
    prev_tf_index = 0
    curr_tf_index = 0

    # start loading frames
    rclpy.init()
    frame_num = 0
    current_retry = 0
    while True:
        if not (test_frames_directory / str(frame_num)).exists():
            break
        current_frame = load_frame_from_directory(
            test_frames_directory / str(frame_num)
        )

        for tf_index in range(prev_tf_index, len(tfs)):
            if tfs[tf_index] == current_frame.inputs.tf:
                curr_tf_index = tf_index
                break

        # publish all tf messages from prev_tf_index to curr_tf_index - 1
        tf_need_to_publish = tfs[prev_tf_index:curr_tf_index]

        expected_output_location = (
            test_frames_directory / str(frame_num) / 'actual_path.bin'
        )

        publisher_node = TestPublisherNode(current_frame, tf_need_to_publish)
        subscriber_node = TestSubscriberNode(expected_output_location)

        executor = MultiThreadedExecutor(num_threads=2)
        executor.add_node(publisher_node)
        executor.add_node(subscriber_node)

        executor_thread = threading.Thread(target=executor.spin, daemon=True)
        executor_thread.start()

        curr_time = time.perf_counter()
        completed = False
        while time.perf_counter() - curr_time < test_case_time_out:
            if (test_frames_directory / str(frame_num) / 'actual_path.bin').exists():
                logger.info(f'Test case {frame_num} completed')
                completed = True

                prev_tf_index = curr_tf_index + 1
                frame_num += 1
                current_retry = 0

                break
            time.sleep(0.1)

        publisher_node.destroy_node()
        subscriber_node.destroy_node()

        if not completed:
            logger.error(f'Test case {frame_num} timed out')
            current_retry += 1

        if current_retry >= maximum_retry:
            logger.error(f'Test case {frame_num} failed after {current_retry} retries')
            prev_tf_index = curr_tf_index + 1
            frame_num += 1
            current_retry = 0
