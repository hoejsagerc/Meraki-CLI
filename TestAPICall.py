import requests
import json
import re


def find_orgid(api_key):

    url = "https://api.meraki.com/api/v1/organizations"

    payload = None

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "X-Cisco-Meraki-API-Key": api_key
    }
    
    response = requests.request('GET', url, headers=headers, data = payload)
    print(response.status_code)
    if response.status_code == 200:
        print("API Call was completed successfully")
    return response.json()[0]['id']




# ----------------------------------------------------------------






#print(find_orgid(api_key))


def get_net_name(org_id, api_key):
    """Function to select a network and store the name and id in a variable

    Args:
        org_id ([Function])-: [Call the function org_id(api_key)]
        api_key ([String]): [API Key proviced by the user]

    Returns:
        [String]: [network_name (name of the network)]
        [String]: [network_id (id of the network)] 
    """
    network_name = input("Select Network: ")

    url = "https://api.meraki.com/api/v1/organizations/{}/networks".format(org_id)

    payload = None

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "X-Cisco-Meraki-API-Key": api_key
    }

    response = requests.request('GET', url, headers=headers, data = payload)

    for net in response.json():
        if net['name'] == network_name:
            print(f"Network: {network_name} has been selected.")
            network_id = net['id']
            return network_name, network_id
        else:
            print("No network with that name was found in your organisation...")


def get_net_id(org_id, api_key, network_name):
    """Function for retrieving the network ID and return it

    Args:
        org_id ([Function])-: [Call the function org_id(api_key)]
        api_key ([String]): [API Key proviced by the user]
        network_name ([String]): [The name of the chosen network]

    Returns:
        [String]: [The network ID]
    """

    url = "https://api.meraki.com/api/v1/organizations/{}/networks".format(org_id)

    payload = None

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "X-Cisco-Meraki-API-Key": api_key
    }

    response = requests.request('GET', url, headers=headers, data = payload)

    print(network_name)




def show_network_switches(net_id, api_key):

    url = "https://api.meraki.com/api/v1/networks/{}/devices".format(net_id)

    payload = None

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "X-Cisco-Meraki-API-Key": api_key
    }

    response = requests.request('GET', url, headers=headers, data = payload)

    print(json.dumps(response.json(), indent=4, sort_keys=True))





def add_device_to_network(net_id, api_key):
    """Function for adding devices to a network. Important note - you may not have
    spaces between the serial numbers when entering them in.

    Args:
        net_id ([String]): [Network ID]
        api_key ([API Key]): [User Provided API Key]
    """

    url = "https://api.meraki.com/api/v1/networks/{}/devices/claim".format(net_id)

    input_serials = input("Enter the serial numbers seperated by ',': ")
    serials = list(input_serials.split(","))

    payload = {
        "serials": serials 
    }

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "X-Cisco-Meraki-API-Key": api_key
    }

    print(json.dumps(payload, indent=4, sort_keys=True))

    response = requests.request('POST', url, headers=headers, data = json.dumps(payload))

    print(response.status_code)

    if response.status_code == 200:
        for serial in serials:
            print(f'Device: {serial} was claimed to the network.')
    else:
        print("An error occured, couldn't claim the devices. Remember you may not have spaces between each serial number.")



def remove_network_device(net_id, api_key):
    """Function for removing devices from a network

    Args:
        net_id ([String]): [Network ID]
        api_key ([String]): [User Provided API Key]
    """

    url = "https://api.meraki.com/api/v1/networks/{}/devices/remove".format(net_id)

    serial = input("Enter the serial number of the device you want to remove: ")

    payload = { "serial": serial }

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "X-Cisco-Meraki-API-Key": api_key
    }

    response = requests.request('POST', url, headers=headers, data = json.dumps(payload))

    if response.status_code == 204:
        print(f"Device {serial} was removed from network.")
    else:
        print("An error occured couldn't remove the device from the network.")



def get_mx_serial(api_key, net_id, mx_name):

    url = "https://api.meraki.com/api/v1/networks/{}/devices".format(net_id)

    payload = None

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "X-Cisco-Meraki-API-Key": api_key
    }

    response = requests.request('GET', url, headers=headers, data = payload)
    print(json.dumps(response.json(), indent=4, sort_keys=True))



def show_mx_interfaces(api_key, net_id):

    url = "https://api.meraki.com/api/v1/networks/{}/appliance/ports".format(net_id)
    vlan_url = "https://api.meraki.com/api/v1/networks/{}/appliance/vlans/settings".format(net_id) 

    payload = None

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "X-Cisco-Meraki-API-Key": api_key
    }
    vlans_enabled = requests.request('GET', vlan_url, headers=headers, data = payload)
    print(vlans_enabled.json())

    if vlans_enabled.json()['vlansEnabled'] == False:
        vlan_payload = '''{ "vlansEnabled": true }'''
        vlan_response = requests.request('PUT', vlan_url, headers=headers, data = vlan_payload)

        print(vlan_response.json())

    response = requests.request('GET', url, headers=headers, data = payload)

    for port in response.json():
        number = str(port['number'])
        enabled = port['enabled']
        port_type = port['type']
        print(f'Interface: {number}      Enabled: {enabled}      Type: {port_type}')










#api_key = "6bec40cf957de430a6f1f2baa056b99a4fac9ea0"
api_key = "c8f989abf579c4f0e39a8115159fa9a6100066cd"
org_id = find_orgid(api_key) 


def show_net_status(api_key, org_id):


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

    #print(response.status_code)
    #print(json.dumps(response.json(), indent=4, sort_keys=True))
    #print(net_name_response.status_code)
    #print(json.dumps(net_name_response.json(), indent=4, sort_keys=True))


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
                        print(f'Public IP: ' +  uplink['ip'])
                        i += 1

                    print("")
                    print("")


    except:
        print("Couldn't retrieve information! Check if you are online...")



net_str = "show network status Azure"

def show_specific_network_status(org_id, api_key, net_str):

    print(net_str.split())
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
    
    print(network_name)
    

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



show_specific_network_status(org_id, api_key, net_str)