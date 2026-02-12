import json
from pathlib import Path
from typing import List

from bs4 import BeautifulSoup, NavigableString
from cyber_record.record import Record
from google.protobuf import text_format

from apollo_modules.modules.planning.proto.planning_pb2 import ADCTrajectory

# from deft.representation.frame import Frame
from deft.representation.trajectory import PathPoint, Trajectory
from deft.utils.apollo_topics import ApolloTopics

LOGGING_FORMAT = (
    '<level>{level.name[0]}{time:MMDD}</level> '
    '<green>{time:HH:mm:ss}</green> '
    '<cyan>{file}:{line}</cyan>] '
    '<bold>{message}</bold>'
)

# def get_last_message_timestamp(f: Frame, candidate_messages):
#     latest_message_timestamp = 0
#     for topic in PLANNING_INPUT_TOPICS:
#         if f.get_sequence_number_for_topic(topic) != -1:
#             latest_message_timestamp = max(
#                 latest_message_timestamp,
#                 candidate_messages[topic][
#                     f.get_sequence_number_for_topic(topic)
#                 ].header.timestamp_sec,
#             )
#     return latest_message_timestamp


def get_vehicle_trajectory(messages_record_path: str):
    record = Record(messages_record_path)
    path_points = []
    for _, msg, _ in record.read_messages(topics=[ApolloTopics.LOCALIZATION]):
        x = msg.pose.position.x
        y = msg.pose.position.y
        t = msg.header.timestamp_sec
        path_point = PathPoint(x, y, 0, 0, t)
        path_points.append(path_point)
    return Trajectory(path_points)


def get_trajectory_from_planning_message(msg) -> Trajectory:
    path_points = []
    for tp in msg.trajectory_point:
        x = tp.path_point.x
        y = tp.path_point.y
        v = tp.v
        a = tp.a
        t = tp.relative_time + msg.header.timestamp_sec
        path_point = PathPoint(x, y, v, a, t)
        path_points.append(path_point)
    return Trajectory(path_points)


def get_trajectory_from_planning_ascii(filename: str) -> Trajectory:
    with open(filename, 'r') as fp:
        msg = text_format.Parse(fp.read(), ADCTrajectory())
        return get_trajectory_from_planning_message(msg)


def get_trajectory_from_planning_bin(filename: str) -> Trajectory:
    result = ADCTrajectory()
    with open(filename, 'rb') as fp:
        result.ParseFromString(fp.read())
    return get_trajectory_from_planning_message(result)


def get_trajectory_from_planning_json(json_path: str) -> Trajectory:
    with open(json_path, 'r') as f:
        data = json.load(f)
    header_timestamp_sec = data['header']['timestampSec']
    path_points = []
    for tp in data['trajectoryPoint']:
        x = tp['pathPoint']['x']
        y = tp['pathPoint']['y']
        v = tp['v']
        a = tp['a']
        t = tp['relativeTime'] + header_timestamp_sec
        path_point = PathPoint(x, y, v, a, t)
        path_points.append(path_point)
    return Trajectory(path_points)


def get_planning_messages(messages_record_path: str) -> List:
    result = []
    record = Record(messages_record_path)
    skip = True
    skip_count = 0
    for _, msg, _ in record.read_messages(topics=[ApolloTopics.PLANNING]):
        if not msg.decision.main_decision.HasField('not_ready'):
            skip = False
        if skip:
            skip_count += 1
            continue
        result.append(msg)
    return result


def compute_coverage_dict(genhtml: Path):
    # find all *.h.gcov.html and *.cpp.gcov.html
    html_files = list(Path(genhtml).rglob('*.gcov.html'))
    result = dict()

    for f in html_files:
        # get f's relative path
        path_name = str(f.relative_to(genhtml))[:-10]

        soup = BeautifulSoup(f.read_text(), 'html.parser')
        source = soup.find('pre', class_='source')
        # iterate over child of source
        current_line_num = -1
        current_line_cov = -1
        coverage_info = dict()
        for child in source.children:
            if isinstance(child, NavigableString):
                continue
            if child.name == 'span':
                if 'lineNum' in child['class']:
                    current_line_num = int(child.text)
                    continue
                if 'lineCov' in child['class']:
                    current_line_cov = int(child.text.split(':')[0])
                    coverage_info[current_line_num] = current_line_cov
                    continue
                if 'lineNoCov' in child['class']:
                    current_line_cov = int(child.text.split(':')[0])
                    coverage_info[current_line_num] = current_line_cov
                    continue
            else:
                lineNum = child.find('span', class_='lineNum')
                if lineNum:
                    current_line_num = int(lineNum.text)

                lineCov = child.find('span', class_='lineCov')
                if lineCov:
                    current_line_cov = int(lineCov.text.split(':')[0])
                    coverage_info[current_line_num] = current_line_cov

                lineNoCov = child.find('span', class_='lineNoCov')
                if lineNoCov:
                    current_line_cov = int(lineNoCov.text.split(':')[0])
                    coverage_info[current_line_num] = current_line_cov

            result[path_name] = coverage_info
    return result


def add_cov(cummulative_cov, new_cov):
    for f in new_cov:
        if f not in cummulative_cov:
            cummulative_cov[f] = dict()
        for ln in new_cov[f]:
            if ln not in cummulative_cov[f]:
                cummulative_cov[f][ln] = new_cov[f][ln]
            else:
                cummulative_cov[f][ln] += new_cov[f][ln]
