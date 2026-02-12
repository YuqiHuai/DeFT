from dataclasses import dataclass
from typing import Tuple

APOLLO_OBSTACLE_TYPE = {
    0: 'UNKNOWN',
    1: 'UNKNOWN_MOVABLE',
    2: 'UNKNOWN_UNMOVABLE',
    3: 'PEDESTRIAN',
    4: 'BICYCLE',
    5: 'VEHICLE',
}


@dataclass
class Obstacle:
    id: int
    type: str
    position: Tuple[float, float, float]
    velocity: Tuple[float, float, float]
    length: float
    width: float
    height: float
    theta: float
