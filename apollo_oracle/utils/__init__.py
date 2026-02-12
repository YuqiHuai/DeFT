import math
from typing import List, Tuple

from apollo_oracle.utils.vehicle_param import VehicleParam


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
    pos_x: float, pos_y: float, pos_z: float, theta: float, vehicle_param: VehicleParam
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
    half_w = vehicle_param.width / 2.0
    front_l = vehicle_param.length - vehicle_param.back2center
    back_l = -1 * vehicle_param.back2center
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
    pos_x: float, pos_y: float, pos_z: float, theta: float, vehicle_param: VehicleParam
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
    half_w = vehicle_param.width / 2.0
    back_l = -1 * vehicle_param.back2center
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
    pos_x: float, pos_y: float, pos_z: float, theta: float, vehicle_param: VehicleParam
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
    half_w = vehicle_param.width / 2.0
    front_l = vehicle_param.length - vehicle_param.back2center
    sin_h = math.sin(theta)
    cos_h = math.cos(theta)
    vectors = [
        (front_l * cos_h - half_w * sin_h, front_l * sin_h + half_w * cos_h),
        (front_l * cos_h + half_w * sin_h, front_l * sin_h - half_w * cos_h),
    ]

    for x, y in vectors:
        points.append((pos_x + x, pos_y + y, pos_z))
    return points
