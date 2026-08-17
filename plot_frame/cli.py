import argparse
from pathlib import Path
from typing import List, Tuple
from datetime import datetime

from matplotlib import pyplot as plt
from apollo_container.utils import generate_adc_polygon, get_vehicle_params
from rich_argparse import RichHelpFormatter
from shapely import LineString
from apollo_modules.modules.planning.proto.planning_pb2 import ADCTrajectory
from apollo_modules.modules.prediction.proto.prediction_obstacle_pb2 import PredictionObstacles
from apollo_modules.modules.map.proto.map_pb2 import Map
from config import CONFIG
import numpy as np

from apollo_modules.modules.localization.proto.localization_pb2 import LocalizationEstimate

OBSTACLE_COLOR = 'green'
EGOCAR_COLOR = 'blue'


def main():
    parser = argparse.ArgumentParser(
        description="Apollo record re-simulation CLI",
        formatter_class=RichHelpFormatter,
    )

    parser.add_argument("frame_dir", help="Directory of module test frame to plot")
    parser.add_argument("map_name", help="Map name")

    args = parser.parse_args()

    frame_dir = Path(args.frame_dir)
    map_name = args.map_name

    print('Plotting frame from directory:', frame_dir)
    print('Using map:', map_name)

    # plt.style.use('dark_background')
    fig, ax = plt.subplots()
    fig.patch.set_facecolor("#F0F0F0")   # outer background
    ax.set_facecolor("#F7F7F7")          # plot area

    map_bin = Path(
        CONFIG.PROJECT_ROOT,
        "data",
        "maps",
        map_name,
        "base_map.bin",
    )

    if not map_bin.exists():
        parser.error(f"Map binary not found: {map_bin}")

    # plot HD map
    
    hdmap = Map()
    with open(map_bin, 'rb') as f:
        hdmap.ParseFromString(f.read())

    boundary_style = {
        0: {"color": "#999999", "linestyle": ":",  "linewidth": 1.5},  # UNKNOWN
        1: {"color": "#E6B800", "linestyle": "--", "linewidth": 2},    # DOTTED_YELLOW
        2: {"color": "#BBBBBB", "linestyle": "--", "linewidth": 2},    # DOTTED_WHITE (FIXED)
        3: {"color": "#E6B800", "linestyle": "-",  "linewidth": 2.5},  # SOLID_YELLOW
        4: {"color": "#BBBBBB", "linestyle": "-",  "linewidth": 2.5},  # SOLID_WHITE (FIXED)
        5: {"color": "#E6B800", "linestyle": "-",  "linewidth": 2},    # DOUBLE_YELLOW
        6: {"color": "#D32F2F", "linestyle": "-",  "linewidth": 3},    # CURB
    }

    for lane in hdmap.lane:
        left_boundary_points = []
        right_boundary_points = []

        for result_container, boundary_obj in [
            (left_boundary_points, lane.left_boundary),
            (right_boundary_points, lane.right_boundary),
        ]:
            for segment in boundary_obj.curve.segment:
                for segment_point in segment.line_segment.point:
                    result_container.append((segment_point.x, segment_point.y))

        left_boundary = LineString(left_boundary_points)
        right_boundary = LineString(right_boundary_points)

        left_type = lane.left_boundary.boundary_type[0].types[0]
        right_type = lane.right_boundary.boundary_type[0].types[0]

        ax = plt.gca()

        # ---- LEFT boundary ----
        if left_type == 5:  # DOUBLE_YELLOW → draw parallel lines inline
            x, y = left_boundary.xy
            x, y = np.array(x), np.array(y)

            dx = np.gradient(x)
            dy = np.gradient(y)
            norm = np.sqrt(dx**2 + dy**2) + 1e-6

            px = -dy / norm * 0.15
            py = dx / norm * 0.15

            ax.plot(x + px, y + py, color="#FFD700", linewidth=2, zorder=3)
            ax.plot(x - px, y - py, color="#FFD700", linewidth=2, zorder=3)
        else:
            style = boundary_style.get(left_type, boundary_style[0])
            ax.plot(*left_boundary.xy, zorder=3, **style)

        # ---- RIGHT boundary ----
        if right_type == 5:  # DOUBLE_YELLOW → draw parallel lines inline
            x, y = right_boundary.xy
            x, y = np.array(x), np.array(y)

            dx = np.gradient(x)
            dy = np.gradient(y)
            norm = np.sqrt(dx**2 + dy**2) + 1e-6

            px = -dy / norm * 0.15
            py = dx / norm * 0.15

            ax.plot(x + px, y + py, color="#FFD700", linewidth=2, zorder=3)
            ax.plot(x - px, y - py, color="#FFD700", linewidth=2, zorder=3)
        else:
            style = boundary_style.get(right_type, boundary_style[0])
            ax.plot(*right_boundary.xy, zorder=3, **style)

    # plot ego car
    loc = LocalizationEstimate()
    with open(frame_dir / 'localization.bin', 'rb') as f:
        loc.ParseFromString(f.read())
    ego_polygon = generate_adc_polygon(
        loc.pose.position.x,
        loc.pose.position.y,
        0.0,
        loc.pose.heading,
        get_vehicle_params(
            str(Path(
                CONFIG.PROJECT_ROOT,
                "data",
                "vehicle_params",
                "Mkz_Example.txt"
            ))    
        ),
    )
    ego_polygon.append(ego_polygon[0])  # close the polygon
    # plot polygon fill with EGOCAR_COLOR
    # fill should be on top of lane boundaries
    plt.fill(
        [p[0] for p in ego_polygon],
        [p[1] for p in ego_polygon],
        color=EGOCAR_COLOR,
        alpha=1.0,
        label='Ego Car',
        zorder=10
    )
    # Zoom in around ego car
    spaces = [40, 10, 10, 40] # left, right, top, bottom
    plt.xlim(loc.pose.position.x - spaces[0], loc.pose.position.x + spaces[1])
    plt.ylim(loc.pose.position.y - spaces[3], loc.pose.position.y + spaces[2])


    # plot ego planning trajectory
    # planning_trajectory = ADCTrajectory()
    # with open(frame_dir / 'deft.bin', 'rb') as f:
    #     planning_trajectory.ParseFromString(f.read())
    
    # pxes, pyes = [], []
    # for trajectory_point in planning_trajectory.trajectory_point:
    #     pxes.append(trajectory_point.path_point.x)
    #     pyes.append(trajectory_point.path_point.y)
    # plt.plot(pxes, pyes, color='red', linewidth=2, label='Planned Trajectory', zorder=5)
    
    # plot obstacles
    prediction_obstacles = PredictionObstacles()
    with open(frame_dir / 'prediction.bin', 'rb') as f:
        prediction_obstacles.ParseFromString(f.read())
    for prediction_obstacle in prediction_obstacles.prediction_obstacle:
        perception_obstacle = prediction_obstacle.perception_obstacle
        obs_polygon = [(p.x, p.y) for p in perception_obstacle.polygon_point]
        obs_polygon.append(obs_polygon[0])  # close the polygon
        plt.fill(
            [p[0] for p in obs_polygon],
            [p[1] for p in obs_polygon],
            color=OBSTACLE_COLOR,
            alpha=0.5,
            label='Obstacle' if 'Obstacle' not in plt.gca().get_legend_handles_labels()[1] else '',
            zorder=8
        )

    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title(f'Map: {map_name}')
    plt.grid()
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    plt.legend()
    plt.savefig(f'frame_plot_{timestamp}.png', dpi=300)
    
    plt.show()
