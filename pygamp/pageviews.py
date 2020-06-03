from .transport import send


def pageview(cid,
             document_path: str = None,
             document_hostname: str = None,
             document_title: str = None):
    """Create a Google Analytics pageview using the Measurement Protocol API.

    :param cid: Client ID
    :param document_path: Document path, i.e. /stuff
    :param document_hostname: Document hostname, i.e. example.com
    :param document_title: Document title, i.e. About us
    :return: HTTP response status
    """

    payload = {
        'cid': cid,
        't': 'pageview',
        'dp': document_path,
        'dh': document_hostname,
        'dt': document_title
    }
    send(payload)
