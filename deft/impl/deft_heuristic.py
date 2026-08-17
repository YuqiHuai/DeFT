import random

from deft.deft_base import DeFTBase
from deft.representation.frame import Frame
from deft.utils.apollo_topics import PLANNING_INPUT_TOPICS, ApolloTopics


class DeFTHeuristic(DeFTBase):
    """
    DeFTHeuristic implements a heuristic-based variant of DeFT that reconstructs
    planning module input frames using time-based inference.

    Instead of relying on system-specific debug information, this implementation
    uses the prediction message as the trigger message and samples a frame creation
    time (tF) between the prediction and planning timestamps. It then applies
    Time-Sensitive Input Search (TISE) heuristics to select, for each input topic,
    the most recent message prior to the sampled time while enforcing temporal
    consistency and monotonicity across frames.
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

        # Sliding pointers + previous selections
        topic_pointers = {topic: 0 for topic in topic_sorted}
        topic_prev_seq = {topic: None for topic in topic_sorted}

        frames = []

        for psn in planning_sequence_numbers:
            planning_msg, _ = planning_messages[psn]
            tP = planning_msg.header.timestamp_sec

            topic_selected_seq = {}

            # Identify trigger message (prediction)
            prediction_time = None
            prediction_seq = None

            if ApolloTopics.PREDICTION in topic_sorted:
                msgs = topic_sorted[ApolloTopics.PREDICTION]
                ptr = topic_pointers[ApolloTopics.PREDICTION]

                while ptr < len(msgs) and msgs[ptr][1][1] / 1e9 <= tP:
                    seq_num, (msg, t) = msgs[ptr]
                    prediction_seq = seq_num
                    prediction_time = t / 1e9  # convert to seconds
                    ptr += 1

                topic_pointers[ApolloTopics.PREDICTION] = ptr

                # Heuristic 3: monotonicity
                prev = topic_prev_seq[ApolloTopics.PREDICTION]
                if prev is not None:
                    if prediction_seq is None:
                        prediction_seq = prev
                    else:
                        prediction_seq = max(prediction_seq, prev)

                if prediction_seq is not None:
                    topic_prev_seq[ApolloTopics.PREDICTION] = prediction_seq

                topic_selected_seq[ApolloTopics.PREDICTION] = prediction_seq

            # sample tF (frame construction time)
            if prediction_time is not None:
                tF = random.uniform(prediction_time, tP)
            else:
                # fallback if prediction not found
                tF = tP

            # perform time-sensitive input search (TISE) for other topics
            for topic, msgs in topic_sorted.items():
                if topic == ApolloTopics.PREDICTION:
                    continue

                ptr = topic_pointers[topic]
                selected_seq = None

                # Find latest message BEFORE tF
                while ptr < len(msgs) and msgs[ptr][1][1] / 1e9 <= tF:
                    seq_num, (msg, _) = msgs[ptr]
                    selected_seq = seq_num
                    ptr += 1

                topic_pointers[topic] = ptr

                # Heuristic 3: monotonicity
                prev = topic_prev_seq[topic]
                if prev is not None:
                    if selected_seq is None:
                        selected_seq = prev
                    else:
                        selected_seq = max(selected_seq, prev)

                # Update state
                if selected_seq is not None:
                    topic_prev_seq[topic] = selected_seq

                topic_selected_seq[topic] = selected_seq

            frame = Frame(
                tF,
                planning_msg.header.sequence_num,
                topic_selected_seq.get(ApolloTopics.ROUTING_RESPONSE),
                topic_selected_seq.get(ApolloTopics.CHASSIS),
                topic_selected_seq.get(ApolloTopics.LOCALIZATION),
                topic_selected_seq.get(ApolloTopics.PREDICTION),
                topic_selected_seq.get(ApolloTopics.TRAFFIC_LIGHT) or 0,
                topic_selected_seq.get(ApolloTopics.STORIES) or 0,
            )
            frames.append(frame)

        return frames
