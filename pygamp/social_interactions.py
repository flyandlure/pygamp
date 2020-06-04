from .transport import send


def social(cid,
           property_id: str,
           social_action: str,
           social_network: str,
           social_target: str):
    """Create a Google Analytics social interaction using the Measurement Protocol API.

    :param cid: Client ID
    :param property_id: Universal Analytics property ID, i.e. UA-123456-1
    :param social_action: Social hit type, i.e. like
    :param social_network: Social network, i.e. facebook
    :param social_target: Social target or document name, i.e. /about-us
    :return: HTTP response status
    """

    payload = {
        'cid': cid,
        't': 'social',
        'social_action': social_action,
        'social_network': social_network,
        'social_target': social_target
    }
    send(payload, property_id)
