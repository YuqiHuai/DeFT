from pathlib import Path
from typing import List

from cyber_record.record import Record

from apollo_modules.modules.canbus.proto.chassis_pb2 import Chassis
from apollo_modules.modules.localization.proto.localization_pb2 import (
    LocalizationEstimate,
)
from apollo_modules.modules.perception.proto.traffic_light_detection_pb2 import (
    TrafficLightDetection,
)
from apollo_modules.modules.prediction.proto.prediction_obstacle_pb2 import (
    PredictionObstacles,
)
from apollo_modules.modules.routing.proto.routing_pb2 import RoutingResponse
from apollo_modules.modules.storytelling.proto.story_pb2 import Stories
from deft.representation.frame import Frame
from deft.utils.apollo_topics import (
    PLANNING_INPUT_TOPICS,
    ApolloTopics,
    get_topic_short_name,
)


def get_empty_message(topic: str):
    """
    Get an empty message for the specified topic.

    Args:
        topic (str): The topic to get the empty message for.

    Returns:
        The empty message for the specified topic.
    """
    if topic == ApolloTopics.ROUTING_RESPONSE:
        return RoutingResponse()
    elif topic == ApolloTopics.CHASSIS:
        return Chassis()
    elif topic == ApolloTopics.LOCALIZATION:
        return LocalizationEstimate()
    elif topic == ApolloTopics.PREDICTION:
        return PredictionObstacles()
    elif topic == ApolloTopics.TRAFFIC_LIGHT:
        return TrafficLightDetection()
    elif topic == ApolloTopics.STORIES:
        return Stories()


class DeFTBase:
    def __init__(self, apollo_root: str):
        """
        Initialize the DeFTBase class.

        Args:
            apollo_root (str): The root directory of the Apollo installation.
        """
        self.apollo_root = Path(apollo_root)
        self.deft_root = Path(self.apollo_root, 'modules', 'deft')
        assert self.deft_root.exists(), 'DeFT is not installed for this apollo version'
        self.ctn_name = 'apollo_dev_deft'
        self.messages = dict()
        self.num_msgs = 0

    def load_record_file(self, record_path: str) -> int:
        """
        Load a record file and extract messages.

        Args:
            record_path (str): The path to the record file.

        Returns:
            int: The number of messages loaded.
        """
        record = Record(record_path)
        self.num_msgs = 0
        start_loading = False
        skip_planning = True

        for topic, msg, t in record.read_messages():
            if topic == ApolloTopics.ROUTING_RESPONSE:
                start_loading = True

            if not start_loading:
                continue

            if (
                topic == ApolloTopics.PLANNING
                and not msg.decision.main_decision.HasField('not_ready')
            ):
                skip_planning = False

            if topic == ApolloTopics.PLANNING and skip_planning:
                continue

            if topic not in self.messages:
                self.messages[topic] = dict()
            sequence_num = msg.header.sequence_num
            self.messages[topic][sequence_num] = (msg, t)
            self.num_msgs += 1
        return self.num_msgs

    def extract_frames(self, record_path: str) -> List[Frame]:
        """
        Extract frames from the loaded messages.

        Args:
            record_path (str): The path to the record file.

        Returns:
            List[Frame]: The extracted frames.
        """
        if not Path(record_path).exists():
            raise FileNotFoundError(record_path)
        num_msgs = self.load_record_file(record_path)
        assert num_msgs > 0, 'No messages loaded'
        assert (
            len(self.messages[ApolloTopics.PLANNING]) > 0
        ), 'No planning messages loaded'

        return self._extract_frames()

    def _extract_frames(self) -> List[Frame]:
        """
        Extract frames from the loaded messages.
        """
        raise NotImplementedError

    def write_frames_to_file(
        self,
        frames: List[Frame],
        testdata_dir: Path,
        write_binary=True,
        write_ascii=False,
    ):
        """
        Write the extracted frames to files.

        Args:
            frames (List[Frame]): The frames to write.
            testdata_dir (Path): The directory to write the files to.
            write_binary (bool): Whether to write binary files.
            write_ascii (bool): Whether to write ASCII files.
        """
        for index, frame in enumerate(frames):
            target_dir = Path(testdata_dir, str(index))
            target_dir.mkdir(parents=True)
            for planning_input_topic in PLANNING_INPUT_TOPICS:
                msg_sequence_num = frame.get_sequence_number_for_topic(
                    planning_input_topic
                )

                # check if input topic is tracked
                if (planning_input_topic not in self.messages) or (
                    msg_sequence_num not in self.messages[planning_input_topic]
                ):
                    msg = get_empty_message(planning_input_topic)
                else:
                    msg, _ = self.messages[planning_input_topic][
                        frame.get_sequence_number_for_topic(planning_input_topic)
                    ]
                topic_short_name = get_topic_short_name(planning_input_topic)

                if write_binary:
                    with open(Path(target_dir, f'{topic_short_name}.bin'), 'wb') as fp:
                        fp.write(msg.SerializeToString())
                if write_ascii:
                    with open(
                        Path(target_dir, f'{topic_short_name}.pb.txt'), 'w'
                    ) as fp:
                        fp.write(str(msg))

            planning_msg, _ = self.messages.get(ApolloTopics.PLANNING).get(
                frame.planning_header_seq
            )
            if write_binary:
                with open(Path(target_dir, 'planning.bin'), 'wb') as fp:
                    fp.write(planning_msg.SerializeToString())
            if write_ascii:
                with open(Path(target_dir, 'planning.pb.txt'), 'w') as fp:
                    fp.write(str(planning_msg))

            deft_header = planning_msg.header
            deft_header.timestamp_sec = frame.timestamp
            if write_binary:
                with open(Path(target_dir, 'header.bin'), 'wb') as fp:
                    fp.write(deft_header.SerializeToString())
            if write_ascii:
                with open(Path(target_dir, 'header.pb.txt'), 'w') as fp:
                    fp.write(str(deft_header))
