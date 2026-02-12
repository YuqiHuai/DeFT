from dataclasses import dataclass
from typing import List

import numpy as np


@dataclass
class PathPoint:
    x: float
    y: float
    v: float
    a: float
    t: float

    def distance_error(self, other: 'PathPoint') -> float:
        """
        Compute the distance error between two PathPoint objects.

        Args:
            other (PathPoint): The other PathPoint object to compare against.

        Returns:
            float: The distance error between the two PathPoint objects.
        """
        return np.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def velocity_error(self, other: 'PathPoint') -> float:
        """
        Compute the velocity error between two PathPoint objects.

        Args:
            other (PathPoint): The other PathPoint object to compare against.

        Returns:
            float: The velocity error between the two PathPoint objects.
        """
        return other.v - self.v

    def acceleration_error(self, other: 'PathPoint') -> float:
        """
        Compute the acceleration error between two PathPoint objects.

        Args:
            other (PathPoint): The other PathPoint object to compare against.

        Returns:
            float: The acceleration error between the two PathPoint objects.
        """
        return other.a - self.a

    def time_error(self, other: 'PathPoint') -> float:
        """
        Compute the time error between two PathPoint objects.

        Args:
            other (PathPoint): The other PathPoint object to compare against.

        Returns:
            float: The time error between the two PathPoint objects.
        """
        return other.t - self.t

    def euclidean_distance(self, other: 'PathPoint') -> float:
        """
        Compute the Euclidean distance between two PathPoint objects.

        Args:
            other (PathPoint): The other PathPoint object to compare against.

        Returns:
            float: The Euclidean distance between the two PathPoint objects.
        """
        return np.sqrt(
            (self.x - other.x) ** 2
            + (self.y - other.y) ** 2
            + (self.v - other.v) ** 2
            + (self.a - other.a) ** 2
            + (self.t - other.t) ** 2
        )


@dataclass
class Trajectory:
    path_points: List[PathPoint]

    def align(self, t: float):
        """
        Align the trajectory by adjusting the time of each path point.
        """
        for pp in self.path_points:
            pp.t -= t

    def displacement(self):
        """
        Compute the displacement of the trajectory.

        Returns:
            float: The displacement of the trajectory.
        """
        if len(self.path_points) == 0:
            return 0.0
        return self.path_points[-1].distance_error(self.path_points[0])

    def length(self):
        """
        Compute the length of the trajectory.

        Returns:
            float: The length of the trajectory.
        """
        total_distance = 0
        for i in range(1, len(self.path_points)):
            prev_x = self.path_points[i - 1].x
            prev_y = self.path_points[i - 1].y
            curr_x = self.path_points[i].x
            curr_y = self.path_points[i].y
            traversed = np.sqrt((prev_x - curr_x) ** 2 + (prev_y - curr_y) ** 2)
            total_distance += traversed
        return total_distance


def eq_traj(x: Trajectory, y: Trajectory, threshold=0.0, compare_time=True) -> bool:
    """
    Check if two trajectories are equivalent within a certain threshold.

    Args:
        x (Trajectory): The first trajectory.
        y (Trajectory): The second trajectory.
        threshold (float, optional): The threshold for equivalence. Defaults to 0.0.
        compare_time (bool, optional): Whether to compare time values. Defaults to True.

    Returns:
        bool: True if the trajectories are equivalent, False otherwise.
    """
    if len(x.path_points) != len(y.path_points):
        return False
    for i in range(len(x.path_points)):
        lhs = x.path_points[i]
        rhs = y.path_points[i]
        if abs(lhs.x - rhs.x) > threshold:
            return False
        if abs(lhs.y - rhs.y) > threshold:
            return False
        if abs(lhs.v - rhs.v) > threshold:
            return False
        if abs(lhs.a - rhs.a) > threshold:
            return False
        if compare_time:
            if abs(lhs.t - rhs.t) > threshold:
                return False
    return True


def euclidean_distance(lhs: Trajectory, rhs: Trajectory, num_data_points=10):
    """
    Compute the Euclidean distance between two trajectories.

    Args:
        lhs (Trajectory): The first trajectory.
        rhs (Trajectory): The second trajectory.
        num_data_points (int): The number of data points to use for interpolation.

    Returns:
        float: The Euclidean distance between the two trajectories.
    """
    lhs_start_t = lhs.path_points[0].t
    lhs_ts = [x.t for x in lhs.path_points]
    lhs_xs = [x.x for x in lhs.path_points]
    lhs_ys = [x.y for x in lhs.path_points]

    rhs_start_t = rhs.path_points[0].t
    rhs_ts = [x.t for x in rhs.path_points]
    rhs_xs = [x.x for x in rhs.path_points]
    rhs_ys = [x.y for x in rhs.path_points]

    lhs_duration = lhs.path_points[-1].t - lhs.path_points[0].t
    rhs_duration = rhs.path_points[-1].t - rhs.path_points[0].t

    min_duration = int(min(lhs_duration, rhs_duration))

    time_points = np.linspace(0, min_duration, num=num_data_points)
    total_distance = 0
    for t in time_points:
        lhs_x = np.interp(t + lhs_start_t, lhs_ts, lhs_xs)
        lhs_y = np.interp(t + lhs_start_t, lhs_ts, lhs_ys)

        rhs_x = np.interp(t + rhs_start_t, rhs_ts, rhs_xs)
        rhs_y = np.interp(t + rhs_start_t, rhs_ts, rhs_ys)
        distance = (lhs_x - rhs_x) ** 2 + (lhs_y - rhs_y) ** 2
        total_distance += distance

    return np.sqrt(total_distance)
