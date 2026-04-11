import pathlib
from typing import List, Optional

import rclpy
from autoware_auto_mapping_msgs.msg import HADMapBin
from autoware_auto_perception_msgs.msg import PredictedObjects, TrafficSignalArray
from autoware_auto_planning_msgs.msg import Path, PathWithLaneId
from diagnostic_msgs.msg import DiagnosticStatus
from geometry_msgs.msg import AccelWithCovarianceStamped
from loguru import logger
from nav_msgs.msg import OccupancyGrid, Odometry
from rclpy.node import Node
from sensor_msgs.msg import PointCloud2
from tier4_planning_msgs.msg import VelocityLimit
from tier4_v2x_msgs.msg import VirtualTrafficLightStateArray
from visualization_msgs.msg import MarkerArray

from deft_autoware.frame import (
    AutowareUnitTestFrame,
    AutowareUnitTestInputs,
    AutowareUnitTestOutput,
    write_frame_to_directory,
)

INPUT_TOPICS = [
    (
        '/planning/scenario_planning/lane_driving/behavior_planning/path_with_lane_id',
        PathWithLaneId,
    ),
    ('/perception/object_recognition/objects', PredictedObjects),
    ('/perception/obstacle_segmentation/pointcloud', PointCloud2),
    ('/localization/kinematic_state', Odometry),
    ('/localization/acceleration', AccelWithCovarianceStamped),
    ('/map/vector_map', HADMapBin),
    ('/perception/occupancy_grid_map/map', OccupancyGrid),
    ('/perception/traffic_light_recognition/traffic_signals', TrafficSignalArray),
    ('/planning/scenario_planning/max_velocity_default', VelocityLimit),
    ('/perception/virtual_traffic_light_states', VirtualTrafficLightStateArray),
]
OUTPUT_TOPICS = [
    ('/planning/scenario_planning/lane_driving/behavior_planning/path', Path),
    ('/planning/scenario_planning/status/stop_reasons', DiagnosticStatus),
    ('/visualization/marker_array', MarkerArray),
]


DeFT_NODE_NAME = 'deft_node'


class DeFT_Autoware(Node):
    def __init__(self, output_directory: pathlib.Path):
        super().__init__(DeFT_NODE_NAME)
        self.output_directory: pathlib.Path = output_directory
        logger.info(
            f'DeFT Node has been initialized. Output directory: {self.output_directory.absolute()}'
        )

        # initialize subscribers for input topics
        self.create_subscription(
            PathWithLaneId,
            '/planning/scenario_planning/lane_driving/behavior_planning/path_with_lane_id',
            self.onPathWithLaneId,
            10,
        )

        self.create_subscription(
            PredictedObjects,
            '/perception/object_recognition/objects',
            self.onPredictedObjects,
            10,
        )

        self.create_subscription(
            PointCloud2,
            '/perception/obstacle_segmentation/pointcloud',
            self.onPointCloud2,
            10,
        )

        self.create_subscription(
            Odometry, '/localization/kinematic_state', self.onOdometry, 10
        )

        self.create_subscription(
            AccelWithCovarianceStamped,
            '/localization/acceleration',
            self.onAccelWithCovarianceStamped,
            10,
        )

        self.create_subscription(HADMapBin, '/map/vector_map', self.onHDMapBin, 10)

        self.create_subscription(
            TrafficSignalArray,
            '/perception/traffic_light_recognition/traffic_signals',
            self.onTrafficSignalArray,
            10,
        )

        self.create_subscription(
            VelocityLimit,
            '/planning/scenario_planning/max_velocity_default',
            self.onVelocityLimit,
            10,
        )

        self.create_subscription(
            VirtualTrafficLightStateArray,
            '/perception/virtual_traffic_light_states',
            self.onVirtualTrafficLightStateArray,
            10,
        )

        self.create_subscription(
            OccupancyGrid,
            '/perception/occupancy_grid_map/map',
            self.onOccupancyGrid,
            10,
        )

        # initialize subscriber for output topic
        self.create_subscription(
            Path,
            '/planning/scenario_planning/lane_driving/behavior_planning/path',
            self.onPath,
            10,
        )

        # initialize class variables for tracking

        self.lastHDMapBin: Optional[HADMapBin] = None
        self.lastPathWithLaneId: Optional[PathWithLaneId] = None
        self.lastPredictedObjects: Optional[PredictedObjects] = None
        self.lastPointCloud2: Optional[PointCloud2] = None
        self.lastOdometry: Optional[Odometry] = None
        self.lastAccelWithCovarianceStamped: Optional[AccelWithCovarianceStamped] = None
        self.lastOccupancyGrid: Optional[OccupancyGrid] = None
        self.lastTrafficSignalArray: Optional[TrafficSignalArray] = None
        self.lastVelocityLimit: Optional[VelocityLimit] = None
        self.lastVirtualTrafficLightStateArray: Optional[
            VirtualTrafficLightStateArray
        ] = None

        self.aggregatedInputs: List[AutowareUnitTestInputs] = []
        self.aggregatedFrames: List[AutowareUnitTestFrame] = []

        self.current_test_id = 'test_id'

    def onPathWithLaneId(self, msg):
        # trigger message
        self.lastPathWithLaneId = msg
        # check if all required inputs have been received
        if (
            self.lastHDMapBin is None
            or self.lastPredictedObjects is None
            or self.lastPointCloud2 is None
            or self.lastOdometry is None
            or self.lastAccelWithCovarianceStamped is None
            or self.lastOccupancyGrid is None
        ):
            logger.error(
                'Trigger received but not all required inputs have been received'
            )
            return
        aggregatedInputs = AutowareUnitTestInputs(
            path_with_lane_id=self.lastPathWithLaneId,
            predicted_objects=self.lastPredictedObjects,
            point_cloud2=self.lastPointCloud2,
            odometry=self.lastOdometry,
            accel_with_covariance_stamped=self.lastAccelWithCovarianceStamped,
            had_map_bin=self.lastHDMapBin,
            occupancy_grid=self.lastOccupancyGrid,
            traffic_signal_array=self.lastTrafficSignalArray,
            velocity_limit=self.lastVelocityLimit,
            virtual_traffic_light_state_array=self.lastVirtualTrafficLightStateArray,
        )
        self.aggregatedInputs.append(aggregatedInputs)
        logger.info('Aggregated inputs')

    def onHDMapBin(self, msg):
        # required for frame (only 1 message is sent at the beginning of the simulation)
        self.lastHDMapBin = msg

        # receiving new HDMapBin indicates a new scenario has started
        # reset the aggregated inputs and frames
        self.aggregatedInputs = []
        self.aggregatedFrames = []

        # use header timestamp as test id
        self.current_test_id = f'test_{msg.header.stamp.sec}_{msg.header.stamp.nanosec}'

        logger.info(f'New scenario started. Test ID: {self.current_test_id}')

    def onPredictedObjects(self, msg):
        # required for frame
        self.lastPredictedObjects = msg

    def onPointCloud2(self, msg):
        # required for frame
        self.lastPointCloud2 = msg

    def onOdometry(self, msg):
        # required for frame
        self.lastOdometry = msg

    def onAccelWithCovarianceStamped(self, msg):
        # required for frame
        self.lastAccelWithCovarianceStamped = msg

    def onOccupancyGrid(self, msg):
        # required for frame
        self.lastOccupancyGrid = msg

    def onTrafficSignalArray(self, msg):
        # not required
        self.lastTrafficSignalArray = msg

    def onVelocityLimit(self, msg):
        # not required
        self.lastVelocityLimit = msg

    def onVirtualTrafficLightStateArray(self, msg):
        # not required
        print('onVirtualTrafficLightStateArray')
        self.lastVirtualTrafficLightStateArray = msg

    def onPath(self, msg):
        # output of the frame has been received

        if len(self.aggregatedInputs) == 0:
            # no input has been aggregated
            logger.error('Output received but no input has been aggregated')
            return
        most_recent_unmatched: AutowareUnitTestInputs = self.aggregatedInputs.pop()

        # create a frame with the first unmatched input and the output
        self.aggregatedFrames.append(
            AutowareUnitTestFrame(most_recent_unmatched, AutowareUnitTestOutput(msg))
        )
        logger.info(f'Aggregated frame. Total frames: {len(self.aggregatedFrames)}')

        # write last frame to disk
        write_frame_to_directory(
            self.aggregatedFrames[-1],
            f'{self.output_directory}/{self.current_test_id}/{len(self.aggregatedFrames) - 1}',
            False,
        )


if __name__ == '__main__':
    rclpy.init(args=None)
    deft_subscriber = DeFT_Autoware()

    rclpy.spin(deft_subscriber)
    rclpy.shutdown()
