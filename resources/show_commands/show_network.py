"""
    NAME
        show_network.py
    CREATED
        23.01.2021
    DESCRIPTION
        This file is for managin all API Calls for 
        Meraki v1 API. This file wil handle all show commands related to
        networks in the Meraki Dashboard.
    UPDATED
        23.01.2021
"""
import json
import requests

__all__ = ['org_id', 'show_net_brf', 'show_net']


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
