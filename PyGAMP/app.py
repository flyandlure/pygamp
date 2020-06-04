from .transport import send


def screenview(cid,
               property_id: str,
               app_name: str,
               app_version: str,
               screen_name: str,
               app_id: str = None,
               app_installer_id: str = None,
               ):
    """Create a Google Analytics app screenview using the Measurement Protocol API.

    :param app_name: Application name
    :param app_installer_id: Application installer ID
    :param app_id: Application ID
    :param screen_name: Screen name, i.e. Home
    :param app_version: Application version number, i.e. 1.0.3
    :param cid: Client ID
    :param property_id: Universal Analytics property ID, i.e. UA-123456-1
    :return: HTTP response status
    """

    payload = {
        'cid': cid,
        't': 'screenview',
        'an': app_name,
        'av': app_version,
        'aid': app_id,
        'aiid': app_installer_id,
        'cd': screen_name
    }
    send(payload, property_id)
