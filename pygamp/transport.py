import requests
import random

ua_property = 'UA-650256-4'
endpoint = 'https://www.google-analytics.com/collect'
user_agent = 'PyGAMP'


def send(payload):
    """Send a payload to Google Analytics using the Measurement Protocol API.

    :param payload: Python dictionary of URL key value pairs
    :return: HTTP response status
    """

    required_payload = {
        'v': 1,
        'tid': ua_property,
        'aip': 1,
        'z': random.random()
    }

    final_payload = {**required_payload, **payload}
    response = requests.post(url=endpoint,
                             data=final_payload,
                             headers={'User-Agent': user_agent},
                             timeout=5.0)
    print(response.request.body)
    return response

