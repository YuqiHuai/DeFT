from deft.deft_base import DeFTBase
from deft.representation.frame import Frame
from deft.utils import ApolloTopics


class DeFTLog(DeFTBase):
    def __init__(self, apollo_root: str):
        super().__init__(apollo_root)

    def _extract_frames(self):
        planning_messages = self.messages[ApolloTopics.PLANNING]
        planning_sequence_numbers = sorted(planning_messages.keys())
        frames = []
        for psn in planning_sequence_numbers:
            msg, t = planning_messages[psn]
            frame = Frame(
                msg.deft.start_timestamp,
                msg.header.sequence_num,
                msg.deft.routing_header,
                msg.deft.chassis_header,
                msg.deft.localization_header,
                msg.deft.prediction_header,
                msg.deft.traffic_light_header,
                msg.deft.stories_header,
            )
            frames.append(frame)
        return frames
