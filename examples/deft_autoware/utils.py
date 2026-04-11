from autoware_auto_mapping_msgs.msg import HADMapBin
from autoware_auto_perception_msgs.msg import PredictedObjects, TrafficSignalArray
from autoware_auto_planning_msgs.msg import Path, PathWithLaneId
from diagnostic_msgs.msg import DiagnosticStatus
from geometry_msgs.msg import AccelWithCovarianceStamped
from nav_msgs.msg import OccupancyGrid, Odometry
from sensor_msgs.msg import PointCloud2
from tier4_planning_msgs.msg import VelocityLimit
from tier4_v2x_msgs.msg import VirtualTrafficLightStateArray
from visualization_msgs.msg import MarkerArray


def msg_to_dict(obj):
    if isinstance(obj, dict):
        return dict((key.lstrip('_'), msg_to_dict(val)) for key, val in obj.items())
    elif hasattr(obj, '_ast'):
        return msg_to_dict(obj._ast())
    elif hasattr(obj, '__iter__') and not isinstance(obj, str):
        return [msg_to_dict(v) for v in obj]
    elif hasattr(obj, '__dict__'):
        return msg_to_dict(vars(obj))
    elif hasattr(obj, '__slots__'):
        return msg_to_dict(
            dict((name, getattr(obj, name)) for name in getattr(obj, '__slots__'))
        )
    return obj


TOPIC_MAP = {
    PathWithLaneId: '/planning/scenario_planning/lane_driving/behavior_planning/path_with_lane_id',
    PredictedObjects: '/perception/object_recognition/objects',
    PointCloud2: '/perception/obstacle_segmentation/pointcloud',
    Odometry: '/localization/kinematic_state',
    AccelWithCovarianceStamped: '/localization/acceleration',
    HADMapBin: '/map/vector_map',
    OccupancyGrid: '/perception/occupancy_grid_map/map',
    TrafficSignalArray: '/perception/traffic_light_recognition/traffic_signals',
    VelocityLimit: '/planning/scenario_planning/max_velocity_default',
    VirtualTrafficLightStateArray: '/perception/virtual_traffic_light_states',
    Path: '/planning/scenario_planning/lane_driving/behavior_planning/path',
    DiagnosticStatus: '/planning/scenario_planning/status/stop_reasons',
    MarkerArray: '/visualization/marker_array',
}


def get_topic_for_type(msg_type):
    return TOPIC_MAP.get(msg_type, None)
