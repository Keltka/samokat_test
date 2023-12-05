import data
import configuration
import requests

def create_order():
    response = requests.post(configuration.BASE_URL + configuration.CREATE_ORDER,
                         json=data.order_body,
                         headers=data.headers)
    track = response.json()["track"]
    assert track
    return track


def get_order(track):
    return requests.get(configuration.BASE_URL + configuration.GET_ORDER,
                        params={"t": track},
                        headers=data.headers)