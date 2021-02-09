import json
import requests

__all__ = ['show_net_brf']


def show_net_brf(org_id, api_key):
    """Function to print all the network names and ID's

    Args:
        org_id ([Function])-: [Call the function org_id(api_key)]
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

    for net in response.json():
        print("Name: " + net['name'] + "\nID: " + net['id'])
        print(" ")