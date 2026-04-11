from deft.deft_base import DeFTBase
from deft.representation.frame import Frame
from deft.utils import ApolloTopics


class DeFTLog(DeFTBase):
    """
    DeFTLog implements a log-assisted variant of DeFT that reconstructs
    planning module input frames directly from pre-recorded DeFT metadata.

    In this implementation, all required input headers (e.g., routing,
    localization, prediction, traffic light) are explicitly stored in the
    log (msg.deft.*). As a result, frame extraction does not require
    Time-Sensitive Input Search (TISE) or heuristic inference.

    This approach provides fully deterministic frame reconstruction, as it
    bypasses message matching and temporal reasoning. However, it relies on
    the availability of logs containing DeFT-specific metadata and is therefore
    not applicable to raw ADS logs.

    This implementation serves as a ground truth reference for validating the
    correctness of more general DeFT approaches.
    """

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
