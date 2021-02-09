import json
import requests

__all__ = ['org_id']


def org_id(api_key):
    """Return the Org ID to provide as argument into other functions

    Args:
        api_key ([String]): [API Key provided by the user]

    Returns:
        [String]: [The Org ID]
    """
    url = "https://api.meraki.com/api/v1/organizations"

    payload = None

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "X-Cisco-Meraki-API-Key": api_key
    }

    response = requests.request('GET', url, headers=headers, data = payload)
    return response.json()[0]['id']