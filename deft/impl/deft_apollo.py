from deft.deft_base import DeFTBase
from deft.representation.frame import Frame
from deft.utils import ApolloTopics


class DeFTApollo(DeFTBase):
    """
    DeFTApollo implements an Apollo-specific variant of DeFT that reconstructs
    planning module input frames deterministically.

    Instead of performing a full Time-Sensitive Input Search (TISE), this
    implementation leverages Apollo planning debug information (e.g., header
    sequence numbers) to directly recover most input messages. TISE-style
    heuristics are only applied where such information is unavailable
    (e.g., traffic light messages).

    This design improves efficiency and determinism compared to the generic
    DeFT approach, at the cost of reduced generality.
    """

    def _extract_frames(self):
        planning_messages = self.messages[ApolloTopics.PLANNING]
        planning_sequence_numbers = sorted(planning_messages.keys())
        frames = []

        traffic_light_msgs = self.messages[ApolloTopics.TRAFFIC_LIGHT]
        traffic_light_keys = sorted(traffic_light_msgs.keys())

        traffic_light_start_index = 0
        prev_traffic_light_header_num = None

        for psn in planning_sequence_numbers:
            pmsg, tP = planning_messages[psn]

            tF = pmsg.deft.start_timestamp  # frame creation time

            # Apollo's planning message contain header sequence numbers
            # that can directly used for TISE.
            routing_header_num = pmsg.debug.planning_data.routing.header.sequence_num
            chassis_header_num = pmsg.debug.planning_data.chassis.header.sequence_num
            localization_header_num = (
                pmsg.debug.planning_data.adc_position.header.sequence_num
            )
            prediction_header_num = (
                pmsg.debug.planning_data.prediction_header.sequence_num
            )

            # Perform TISE for traffic light messages using heuristics:
            traffic_light_header_num = None
            best_idx = traffic_light_start_index

            # find latest message BEFORE tF (preferred)
            for i in range(traffic_light_start_index, len(traffic_light_keys)):
                key = traffic_light_keys[i]
                tl_msg, tl_time = traffic_light_msgs[key]
                tl_time = tl_time / 1e9  # convert to seconds
                print(tl_time, i)
                if tl_time <= tF:
                    traffic_light_header_num = tl_msg.header.sequence_num
                    best_idx = i
                else:
                    break  # since sorted by time

            # Heuristic 3: non-decreasing sequence number
            if prev_traffic_light_header_num is not None:
                if traffic_light_header_num is None:
                    traffic_light_header_num = prev_traffic_light_header_num
                else:
                    traffic_light_header_num = max(
                        traffic_light_header_num, prev_traffic_light_header_num
                    )

            # Update state
            if traffic_light_header_num is not None:
                prev_traffic_light_header_num = traffic_light_header_num
                traffic_light_start_index = best_idx

            # Stories not supported by current test approaches
            stories_header_num = 0

            frame = Frame(
                tF,
                pmsg.header.sequence_num,
                routing_header_num,
                chassis_header_num,
                localization_header_num,
                prediction_header_num,
                traffic_light_header_num or 0,  # fallback to 0 if no TL message found
                stories_header_num,
            )
            frames.append(frame)
        return frames
