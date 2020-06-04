from .transport import send


def event(cid,
          property_id: str,
          category: str,
          action: str,
          label: str = None,
          value: int = None,
          non_interactive: int = 0):
    """Create a Google Analytics event using the Measurement Protocol API.

    :param cid: Client ID
    :param property_id: Universal Analytics property ID, i.e. UA-123456-1
    :param category: Event category string
    :param action: Event action string
    :param label: Optional event label string
    :param value: Optional event value integer
    :param non_interactive: Specify whether the hit type is non-interactive by passing 1
    :return: HTTP response status
    """

    payload = {
        'cid': cid,
        't': 'event',
        'ec': category,
        'ea': action,
        'el': label,
        'ev': str(int(value)),
        'ni': non_interactive
    }
    send(payload, property_id)
