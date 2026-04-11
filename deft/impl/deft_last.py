from deft.deft_base import DeFTBase
from deft.representation.frame import Frame
from deft.utils.apollo_topics import PLANNING_INPUT_TOPICS, ApolloTopics


class DeFTLast(DeFTBase):
    """
    DeFTLast implements a heuristic-based variant of DeFT that reconstructs
    planning module input frames by selecting the most recent message from
    each input topic prior to each planning execution.

    This implementation approximates the Time-Sensitive Input Search (TISE)
    by maintaining sliding pointers over time-sorted message streams for each
    input topic. For every planning message, it advances each topic pointer
    to include all messages with timestamps less than or equal to the planning
    time, and records the latest observed sequence number as the input.

    This approach enforces temporal consistency (messages must occur before
    the planning step) and implicitly follows the "latest message" heuristic
    described in DeFT. In practice, this method yield module-tests that are invalid
    due to latest message from a channel violating constraint of tF (i.e., the
    frame-construction time).
    """

    def _extract_frames(self):
        planning_messages = self.messages[ApolloTopics.PLANNING]
        planning_sequence_numbers = sorted(planning_messages.keys())

        # Pre-sort topic messages by timestamp
        topic_sorted = {}
        for topic in PLANNING_INPUT_TOPICS:
            if topic in self.messages:
                topic_sorted[topic] = sorted(
                    self.messages[topic].items(),
                    key=lambda x: x[1][1],  # sort by timestamp
                )

        # Initialize sliding pointers per topic
        topic_pointers = {topic: 0 for topic in topic_sorted}
        topic_latest_seq = {topic: None for topic in topic_sorted}

        frames = []

        for psn in planning_sequence_numbers:
            planning_msg, planning_time = planning_messages[psn]
            planning_time = planning_msg.header.timestamp_sec

            # Slide each topic pointer forward
            for topic, msgs in topic_sorted.items():
                ptr = topic_pointers[topic]
                while ptr < len(msgs) and msgs[ptr][1][1] / 1e9 <= planning_time:
                    seq_num, (msg, t) = msgs[ptr]
                    topic_latest_seq[topic] = seq_num
                    ptr += 1
                topic_pointers[topic] = ptr

            frame = Frame(
                planning_time,
                planning_msg.header.sequence_num,
                topic_latest_seq.get(ApolloTopics.ROUTING_RESPONSE),
                topic_latest_seq.get(ApolloTopics.CHASSIS),
                topic_latest_seq.get(ApolloTopics.LOCALIZATION),
                topic_latest_seq.get(ApolloTopics.PREDICTION),
                topic_latest_seq.get(ApolloTopics.TRAFFIC_LIGHT),
                topic_latest_seq.get(ApolloTopics.STORIES),
            )

            frames.append(frame)

        return frames
