import json
import requests

__all__ = ['show_net']


def show_net(org_id, api_key):
    """Function for prinrint in json, verbose info on all networks names

    Args:
        org_id ([String]): [Call the function org_id(api_key)]
        api_key ([String]): [API Key proviced by the user]
    """
    url = "https://api.meraki.com/api/v1/organizations/{}/networks".format(org_id)

    payload = None

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "X-Cisco-Meraki-API-Key": api_key
    }

    response = requests.request('GET', url, headers=headers, data = payload)
    print(json.dumps(response.json(), indent=4, sort_keys=True))