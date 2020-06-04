from .transport import send


def exception(cid,
              property_id: str,
              exception_description: str,
              exception_fatal: int = 1):
    """Create a Google Analytics exception using the Measurement Protocol API.

    :param cid: Client ID
    :param property_id: Universal Analytics property ID, i.e. UA-123456-1
    :param exception_description: Description of exception, i.e. 'Transaction not found'
    :param exception_fatal: Pass a 1 value for fatal exceptions or a zero for non-fatal
    :return: HTTP response status
    """

    payload = {
        'cid': cid,
        't': 'exception',
        'exd': exception_description,
        'exf': exception_fatal,
    }
    send(payload, property_id)
