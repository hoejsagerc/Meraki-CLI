import json
import requests

__all__ = ['show_network_switches']


def show_network_switches(net_id, api_key, brief: bool = False):
    """Function for showing verbose or brief information on all switches in a network

    Args:
        net_id ([String]): [Network ID]
        api_key ([String]): [The user provided API Key]
        brief ([Boolean]): [If False the function will output verbose and if True it will output brief] 
    """

    url = "https://api.meraki.com/api/v1/networks/{}/devices".format(net_id)

    payload = None

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "X-Cisco-Meraki-API-Key": api_key
    }

    response = requests.request('GET', url, headers=headers, data = payload)

    try:
        if brief == False:
            for net in response.json():
                if "MS" in net['model']:
                    print(json.dumps(net, indent=4, sort_keys=True))
        
        elif brief == True:
            for net in response.json():
                if "MS" in net['model']:
                    print("Switch Name: " + net['name'])
                    print("Switch Model: " + net['model'])
                    print("Switch Serial: " + net['serial'])
                    print("Switch IP: " + net['lanIp'])
                    print(" ")
    except:
        print("An error occured, couldn't fetch Switches")