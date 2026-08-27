from pathlib import Path
from typing import Dict, List

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
    def __init__(self):
        """
        Initialize the DeFTBase class.

        Args:
            apollo_root (str): The root directory of the Apollo installation.
        """
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

            if topic == ApolloTopics.PLANNING:
                # Frames are derived from planning outputs, so only accept
                # those belonging to the current route and reporting a real
                # decision.
                if not start_loading:
                    continue

                if not msg.decision.main_decision.HasField('not_ready'):
                    skip_planning = False

                if skip_planning:
                    continue

            # Planning inputs are kept regardless of when they were published.
            # The first planning frames of a route routinely reference chassis
            # and localization messages recorded microseconds *before* the
            # routing response; discarding those left those frames with empty
            # inputs and made them unreproducible.

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
        # Frame indices that had to fall back to an empty input message even
        # though the topic was recorded. Such frames cannot reproduce the
        # recorded planning output, so they are reported to the caller.
        missing_inputs: Dict[str, List[int]] = dict()

        for index, frame in enumerate(frames):
            target_dir = Path(testdata_dir, str(index))
            target_dir.mkdir(parents=True)
            for planning_input_topic in PLANNING_INPUT_TOPICS:
                msg_sequence_num = frame.get_sequence_number_for_topic(
                    planning_input_topic
                )
                topic_short_name = get_topic_short_name(planning_input_topic)
                topic_messages = self.messages.get(planning_input_topic)

                # check if input topic is tracked
                if topic_messages is None:
                    # The topic is absent from the whole record, which is a
                    # property of the scenario rather than lost input data.
                    msg = get_empty_message(planning_input_topic)
                elif msg_sequence_num not in topic_messages:
                    # The topic was recorded but the message this frame refers
                    # to was not retained: the frame loses real input data.
                    msg = get_empty_message(planning_input_topic)
                    missing_inputs.setdefault(topic_short_name, []).append(index)
                else:
                    msg, _ = topic_messages[msg_sequence_num]

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

        self._warn_about_missing_inputs(missing_inputs, len(frames))

    @staticmethod
    def _warn_about_missing_inputs(
        missing_inputs: Dict[str, List[int]], num_frames: int
    ):
        """
        Report frames that were written with empty planning inputs.

        Args:
            missing_inputs (Dict[str, List[int]]): Frame indices per input
                topic that fell back to an empty message.
            num_frames (int): Total number of frames written.
        """
        if not missing_inputs:
            return

        affected = sorted({i for indices in missing_inputs.values() for i in indices})
        print(
            f'WARNING: {len(affected)} of {num_frames} frames were written with '
            'empty planning inputs and will not reproduce the recorded planning '
            'output:'
        )
        for topic_short_name in sorted(missing_inputs):
            indices = missing_inputs[topic_short_name]
            shown = ', '.join(str(i) for i in indices[:10])
            if len(indices) > 10:
                shown += f', ... (+{len(indices) - 10} more)'
            print(f'    {topic_short_name:<14}: {len(indices)} frame(s) [{shown}]')
