import math
import shutil
from dataclasses import dataclass
from pathlib import Path
from typing import List, Tuple

from google.protobuf import text_format

# from config import APOLLO_FLAGFILE, APOLLO_ROOT, MAPS_DIR, SUPPORTED_MAPS
from apollo_modules.modules.common.configs.proto.vehicle_config_pb2 import VehicleConfig


@dataclass
class ApolloVehicleConfig:
    length: int
    width: int
    height: int
    front_edge_to_center: int
    back_edge_to_center: int
    left_edge_to_center: int
    right_edge_to_center: int


def get_vehicle_params(vehicle_param_file: str) -> ApolloVehicleConfig:
    with open(vehicle_param_file, 'r') as fp:
        v = text_format.Parse(fp.read(), VehicleConfig())
        print(v)
    return ApolloVehicleConfig(
        length=v.vehicle_param.length,
        width=v.vehicle_param.width,
        height=v.vehicle_param.height,
        front_edge_to_center=v.vehicle_param.front_edge_to_center,
        back_edge_to_center=v.vehicle_param.back_edge_to_center,
        left_edge_to_center=v.vehicle_param.left_edge_to_center,
        right_edge_to_center=v.vehicle_param.right_edge_to_center,
    )


def clean_apollo_logs(apollo_root):
    data_dir = Path(apollo_root, 'data')
    if data_dir.exists():
        shutil.rmtree(data_dir)
    for log_file in Path(apollo_root).glob('*.log.*'):
        log_file.unlink()


def change_apollo_map(apollo_root: str, map_name: str, map_dir: str) -> None:
    """
    Change the map used by Apollo
    :param str map_name: name of the map to use
    """
    apollo_flagfile = Path(apollo_root, 'modules/common/data/global_flagfile.txt')
    if apollo_flagfile.exists():
        with open(apollo_flagfile, 'a') as fp:
            fp.write(f'\n--map_dir=/apollo/modules/map/data/{map_name}\n')

        apollo_map_dir = Path(apollo_root, 'modules', 'map', 'data', map_name)
        apollo_map_dir.parent.mkdir(parents=True, exist_ok=True)
        if not apollo_map_dir.exists():
            shutil.copytree(
                map_dir,
                apollo_map_dir,
            )


def generate_polygon(
    pos_x: float, pos_y: float, pos_z: float, theta: float, length: float, width: float
) -> List[Tuple[float, float, float]]:
    """
    Generate polygon for a perception obstacle
    :param float pos_x: x position of the obstacle
    :param float pos_y: y position of the obstacle
    :param float pos_z: z position of the obstacle
    :param float theta: heading of the obstacle
    :param float length: length of the obstacle
    :param float width: width of the obstacle
    :return: list of points
    """
    points: List[Tuple[float, float, float]] = []
    half_l = length / 2.0
    half_w = width / 2.0
    sin_h = math.sin(theta)
    cos_h = math.cos(theta)
    vectors = [
        (half_l * cos_h - half_w * sin_h, half_l * sin_h + half_w * cos_h),
        (-half_l * cos_h - half_w * sin_h, -half_l * sin_h + half_w * cos_h),
        (-half_l * cos_h + half_w * sin_h, -half_l * sin_h - half_w * cos_h),
        (half_l * cos_h + half_w * sin_h, half_l * sin_h - half_w * cos_h),
    ]
    for x, y in vectors:
        points.append((pos_x + x, pos_y + y, pos_z))
    return points


def generate_adc_polygon(
    pos_x: float,
    pos_y: float,
    pos_z: float,
    theta: float,
    vehicle_cfg: ApolloVehicleConfig,
) -> List[Tuple[float, float, float]]:
    """
    Generate a polygon for the ADC based on its current position
    :param float pos_x: x position of the ADC
    :param float pos_y: y position of the ADC
    :param float pos_z: z position of the ADC
    :param float theta: the heading of the ADC (in radians)
    :returns: a list consisting 4 tuples to represent the polygon of the ADC
    """

    points = []
    half_w = vehicle_cfg.width / 2.0
    front_l = vehicle_cfg.length - vehicle_cfg.back_edge_to_center
    back_l = -1 * vehicle_cfg.back_edge_to_center
    sin_h = math.sin(theta)
    cos_h = math.cos(theta)
    vectors = [
        (front_l * cos_h - half_w * sin_h, front_l * sin_h + half_w * cos_h),
        (back_l * cos_h - half_w * sin_h, back_l * sin_h + half_w * cos_h),
        (back_l * cos_h + half_w * sin_h, back_l * sin_h - half_w * cos_h),
        (front_l * cos_h + half_w * sin_h, front_l * sin_h - half_w * cos_h),
    ]
    for x, y in vectors:
        points.append((pos_x + x, pos_y + y, pos_z))
    return points


def generate_adc_rear_vertices(
    pos_x: float,
    pos_y: float,
    pos_z: float,
    theta: float,
    vehicle_cfg: ApolloVehicleConfig,
) -> List[Tuple[float, float, float]]:
    """
    Generate the rear edge for the ADC
    :param float pos_x: x position of the ADC
    :param float pos_y: y position of the ADC
    :param float pos_z: z position of the ADC
    :param float theta: the heading of the ADC (in radians)
    :returns: a list consisting 2 tuples to represent the rear edge of the ADC
    """
    points = []
    half_w = vehicle_cfg.width / 2.0
    back_l = -1 * vehicle_cfg.back_edge_to_center
    sin_h = math.sin(theta)
    cos_h = math.cos(theta)
    vectors = [
        (back_l * cos_h - half_w * sin_h, back_l * sin_h + half_w * cos_h),
        (back_l * cos_h + half_w * sin_h, back_l * sin_h - half_w * cos_h),
    ]

    for x, y in vectors:
        points.append((pos_x + x, pos_y + y, pos_z))
    return points


def generate_adc_front_vertices(
    pos_x: float,
    pos_y: float,
    pos_z: float,
    theta: float,
    vehicle_cfg: ApolloVehicleConfig,
) -> List[Tuple[float, float, float]]:
    """
    Generate the rear edge for the ADC
    :param float pos_x: x position of the ADC
    :param float pos_y: y position of the ADC
    :param float pos_z: z position of the ADC
    :param float theta: the heading of the ADC (in radians)
    :returns: a list consisting 2 tuples to represent the rear edge of the ADC
    """
    points = []
    half_w = vehicle_cfg.width / 2.0
    front_l = vehicle_cfg.length - vehicle_cfg.back_edge_to_center
    sin_h = math.sin(theta)
    cos_h = math.cos(theta)
    vectors = [
        (front_l * cos_h - half_w * sin_h, front_l * sin_h + half_w * cos_h),
        (front_l * cos_h + half_w * sin_h, front_l * sin_h - half_w * cos_h),
    ]

    for x, y in vectors:
        points.append((pos_x + x, pos_y + y, pos_z))
    return points
