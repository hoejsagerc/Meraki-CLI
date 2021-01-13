import json
import requests
from prompt_toolkit.formatted_text import HTML

def con_toolbox(api_key):
    url = "https://api.meraki.com/api/v1/organizations"

    payload = None

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "X-Cisco-Meraki-API-Key": api_key
    }

    response = requests.request('GET', url, headers=headers, data = payload)
    org = response.json()[0]['name']
    return HTML('Organisation: <b><style bg="ansired">{}</style></b>!'.format(org))


def org_id(api_key):
    url = "https://api.meraki.com/api/v1/organizations"

    payload = None

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "X-Cisco-Meraki-API-Key": api_key
    }

    response = requests.request('GET', url, headers=headers, data = payload)
    return response.json()[0]['id']


def show_networks(org_id, api_key):
    url = "https://api.meraki.com/api/v1/organizations/{}/networks".format(org_id)

    payload = None

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "X-Cisco-Meraki-API-Key": api_key
    }

    response = requests.request('GET', url, headers=headers, data = payload)

    for net in response.json():
        print("Name: " + net['name'])


def show_run_networks(org_id, api_key):
    url = "https://api.meraki.com/api/v1/organizations/{}/networks".format(org_id)

    payload = None

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "X-Cisco-Meraki-API-Key": api_key
    }

    response = requests.request('GET', url, headers=headers, data = payload)
    print(json.dumps(response.json(), indent=4, sort_keys=True))


def r_prompt(network_name):
    if network_name == "none":
        return f'<None>'
    else:    
        return f'<{network_name}>'






#show_run_networks("671599294431626151", "665c5bb8b79175eaf9c1be01e0c4f67ed5959020")