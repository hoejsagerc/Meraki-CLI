import json
import requests

__all__ = ['show_net_status', 'show_specific_network_status']



def show_net_status(org_id, api_key):
    """Function for retriving information on which networks are offline or online

    Args:
        api_key (String): [User provided API Key]
        org_id ([Function]): [Organisation Id found from function]
    """

    url = "https://api.meraki.com/api/v1/organizations/{}/appliance/uplink/statuses".format(org_id)
    net_name_url = "https://api.meraki.com/api/v1/organizations/{}/networks".format(org_id)

    payload = None

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "X-Cisco-Meraki-API-Key": api_key
    }

    response = requests.request('GET', url, headers=headers, data = payload)
    net_name_response = requests.request('GET', net_name_url, headers=headers, data = payload)

    try:

        for resp in response.json():
            for net in net_name_response.json():
                
                if resp['networkId'] == net['id']:
                    print(f'Network: ' + net['name'])
                    print(f'Last Uplink Report: ' + resp['lastReportedAt'])
                    i = 1
                    for uplink in resp['uplinks']:
                        print(f'Uplink: {i}')
                        print(f'Status: ' + uplink['status'])
                        print(f'Interface: ' + uplink['interface'])
                        print(f'Public IP: ' +  str(uplink['ip']))
                        i += 1

                    print("")
                    print("")

    except:
        print("Couldn't retrieve information! Check if you are online...")


def show_specific_network_status(org_id, api_key, net_str):
    """Functino for findin network status on one specific network

    Args:
        org_id (Function): Function prvided in main
        api_key (String): User provided API Key
        net_str (String): String from the user prompt containing the network name. Case sensitive.
    """

    network = net_str.split()
    if len(net_str.split()) > 3:
        index_len = len(net_str)
        network_name = ""
#       if len(net_str.split()) > 2:
        for x in net_str.split()[3:index_len + 1]:
            network_name += x
            network_name += " "
        network_name = network_name.rstrip()
    else:
        network_name = net_str.spli()[3]
    

    url = "https://api.meraki.com/api/v1/organizations/{}/appliance/uplink/statuses".format(org_id)
    net_name_url = "https://api.meraki.com/api/v1/organizations/{}/networks".format(org_id)

    payload = None

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "X-Cisco-Meraki-API-Key": api_key
    }

    response = requests.request('GET', url, headers=headers, data = payload)
    net_name_response = requests.request('GET', net_name_url, headers=headers, data = payload)


    try:
        for net in net_name_response.json():
            if net['name'] == network_name:
                network_id = net['id']

        for resp in response.json():
            if resp['networkId'] == network_id:
                print(f'Network: {network_name}')
                print(f'Last Uplink Report: ' + resp['lastReportedAt'])
                i = 1
                for uplink in resp['uplinks']:
                    print(f'Uplink: {i}')
                    print(f'Status: ' + uplink['status'])
                    print(f'Interface: ' + uplink['interface'])
                    print(f'Public IP: ' +  str(uplink['ip']))
                    i += 1
    except:
        print("Couldn't retrieve information! Check if you are online...")

