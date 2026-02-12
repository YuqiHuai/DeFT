from deft.deft_base import DeFTBase
from deft.representation.frame import Frame
from deft.utils.apollo_topics import PLANNING_INPUT_TOPICS, ApolloTopics


class DeFTLast(DeFTBase):

    def __init__(self, apollo_root: str):
        super().__init__(apollo_root)

    def _extract_frames(self):

        planning_messages = self.messages[ApolloTopics.PLANNING]
        planning_sequence_numbers = sorted(planning_messages.keys())

        # Pre-sort topic messages by timestamp
        topic_sorted = {}
        for topic in PLANNING_INPUT_TOPICS:
            if topic in self.messages:
                topic_sorted[topic] = sorted(
                    self.messages[topic].items(),
                    key=lambda x: x[1][1]  # sort by timestamp
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
                while ptr < len(msgs) and msgs[ptr][1][1]/1e9 <= planning_time:
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
