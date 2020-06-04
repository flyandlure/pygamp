import requests
import random

endpoint = 'https://www.google-analytics.com/collect'
user_agent = 'pygamp'


def send(payload, property_id):
    """Send a payload to Google Analytics using the Measurement Protocol API.

    :param payload: Python dictionary of URL key value pairs
    :param property_id: Universal Analytics property ID, i.e. UA-123456-1
    :return: HTTP response status
    """

    required_payload = {
        'v': 1,
        'tid': property_id,
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

