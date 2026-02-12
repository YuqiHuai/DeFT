from dataclasses import dataclass

from deft.utils.apollo_topics import ApolloTopics


@dataclass
class Frame:
    timestamp: float
    planning_header_seq: int
    routing_header_seq: int
    chassis_header_seq: int
    localization_header_seq: int
    prediction_header_seq: int
    traffic_light_header_seq: int
    stories_header_seq: int = -1

    def json(self):
        """
        Convert the Frame object to a JSON-serializable dictionary.

        Returns:
            A JSON-serializable dictionary representation of the Frame object.
        """
        return {
            'timestamp': self.timestamp,
            'planning_header_seq': self.planning_header_seq,
            'routing_header_seq': self.routing_header_seq,
            'chassis_header_seq': self.chassis_header_seq,
            'localization_header_seq': self.localization_header_seq,
            'prediction_header_seq': self.prediction_header_seq,
            'traffic_light_header_seq': self.traffic_light_header_seq,
            'stories_header_seq': self.stories_header_seq,
        }

    def __hash__(self) -> int:
        """
        Compute a hash of the Frame object.

        Returns:
            An integer hash of the Frame object.
        """
        return hash(
            (
                self.timestamp,
                self.planning_header_seq,
                self.routing_header_seq,
                self.chassis_header_seq,
                self.localization_header_seq,
                self.prediction_header_seq,
                self.traffic_light_header_seq,
                self.stories_header_seq,
            )
        )

    def set_sequence_number_for_topic(self, topic: ApolloTopics, seq: int) -> None:
        """
        Set the sequence number for a specific topic.

        Args:
            topic (ApolloTopics): The topic for which to set the sequence number.
            seq (int): The sequence number to set.
        """
        if topic == ApolloTopics.ROUTING_RESPONSE:
            self.routing_header_seq = seq
        elif topic == ApolloTopics.CHASSIS:
            self.chassis_header_seq = seq
        elif topic == ApolloTopics.LOCALIZATION:
            self.localization_header_seq = seq
        elif topic == ApolloTopics.PREDICTION:
            self.prediction_header_seq = seq
        elif topic == ApolloTopics.TRAFFIC_LIGHT:
            self.traffic_light_header_seq = seq
        elif topic == ApolloTopics.STORIES:
            self.stories_header_seq = seq

    def get_sequence_number_for_topic(self, topic: ApolloTopics) -> int:
        """
        Get the sequence number for a specific topic.

        Args:
            topic (ApolloTopics): The topic for which to get the sequence number.

        Returns:
            int: The sequence number for the specified topic.
        """
        if topic == ApolloTopics.ROUTING_RESPONSE:
            return self.routing_header_seq
        elif topic == ApolloTopics.CHASSIS:
            return self.chassis_header_seq
        elif topic == ApolloTopics.LOCALIZATION:
            return self.localization_header_seq
        elif topic == ApolloTopics.PREDICTION:
            return self.prediction_header_seq
        elif topic == ApolloTopics.TRAFFIC_LIGHT:
            return self.traffic_light_header_seq
        elif topic == ApolloTopics.STORIES:
            return self.stories_header_seq
