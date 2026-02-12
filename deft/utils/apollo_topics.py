class ApolloTopics:
    ROUTING_RESPONSE = '/apollo/routing_response'
    CHASSIS = '/apollo/canbus/chassis'
    LOCALIZATION = '/apollo/localization/pose'
    PREDICTION = '/apollo/prediction'
    TRAFFIC_LIGHT = '/apollo/perception/traffic_light'
    PLANNING = '/apollo/planning'
    STORIES = '/apollo/storytelling'


PLANNING_INPUT_TOPICS = [
    ApolloTopics.ROUTING_RESPONSE,
    ApolloTopics.CHASSIS,
    ApolloTopics.LOCALIZATION,
    ApolloTopics.PREDICTION,
    ApolloTopics.TRAFFIC_LIGHT,
    ApolloTopics.STORIES,
]


def get_topic_short_name(topic: ApolloTopics) -> str:
    if topic == ApolloTopics.ROUTING_RESPONSE:
        return 'routing'
    elif topic == ApolloTopics.CHASSIS:
        return 'chassis'
    elif topic == ApolloTopics.LOCALIZATION:
        return 'localization'
    elif topic == ApolloTopics.PREDICTION:
        return 'prediction'
    elif topic == ApolloTopics.TRAFFIC_LIGHT:
        return 'traffic_light'
    elif topic == ApolloTopics.PLANNING:
        return 'planning'
    elif topic == ApolloTopics.STORIES:
        return 'stories'
