import json
import requests

__all__ = ['show_l3_firewall_rules', 'show_l3_firewall_block_rules', 'show_l3_firewall_allow_rules']


def show_l3_firewall_rules(api_key, net_id):

    url = "https://api.meraki.com/api/v1/networks/{}/appliance/firewall/l3FirewallRules".format(net_id)

    payload = None

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "X-Cisco-Meraki-API-Key": api_key
    }

    response = requests.request('GET', url, headers=headers, data = payload)
    
    if response.status_code == 200:
        i = 0
        for x in response.json()['rules']:
            print(f'RULE #{i} - Name: ' + str(x['comment']))
            print("--------------------------------------------------")
            print(f'    policy:            ' + str(x['policy']))
            print(f'    protocol:          ' + str(x['protocol']))
            print(f'    Source port:       ' + str(x['srcPort']))
            print(f'    Destination port:  ' + str(x['destPort']))
            print(f'    Source addr:       ' + str(x['srcCidr']))
            print(f'    Destonation addr:  ' + str(x['destCidr']))
            print(f'    Syslgog enabled:   ' + str(x['syslogEnabled']))
            print("")
            print("")
            i += 1
    
    return response.status_code


def show_l3_firewall_block_rules(api_key, net_id):

    url = "https://api.meraki.com/api/v1/networks/{}/appliance/firewall/l3FirewallRules".format(net_id)

    payload = None

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "X-Cisco-Meraki-API-Key": api_key
    }

    response = requests.request('GET', url, headers=headers, data = payload)
    
    if response.status_code == 200:
        for x in response.json()['rules']:
            i = 0
            if x['policy'] == 'deny':
                print(f'RULE #{i} - Name: ' + str(x['comment']))
                print("--------------------------------------------------")
                print(f'    policy:            ' + str(x['policy']))
                print(f'    protocol:          ' + str(x['protocol']))
                print(f'    Source port:       ' + str(x['srcPort']))
                print(f'    Destination port:  ' + str(x['destPort']))
                print(f'    Source addr:       ' + str(x['srcCidr']))
                print(f'    Destonation addr:  ' + str(x['destCidr']))
                print(f'    Syslgog enabled:   ' + str(x['syslogEnabled']))
                print("")
                print("")
                i += 1
    
    return response.status_code


def show_l3_firewall_allow_rules(api_key, net_id):

    url = "https://api.meraki.com/api/v1/networks/{}/appliance/firewall/l3FirewallRules".format(net_id)

    payload = None

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "X-Cisco-Meraki-API-Key": api_key
    }

    response = requests.request('GET', url, headers=headers, data = payload)
    
    if response.status_code == 200:
        i = 0
        for x in response.json()['rules']:
            if x['policy'] == 'allow':
                print(f'RULE #{i} - Name: ' + str(x['comment']))
                print("--------------------------------------------------")
                print(f'    policy:            ' + str(x['policy']))
                print(f'    protocol:          ' + str(x['protocol']))
                print(f'    Source port:       ' + str(x['srcPort']))
                print(f'    Destination port:  ' + str(x['destPort']))
                print(f'    Source addr:       ' + str(x['srcCidr']))
                print(f'    Destonation addr:  ' + str(x['destCidr']))
                print(f'    Syslgog enabled:   ' + str(x['syslogEnabled']))
                print("")
                print("")
                i += 1

        return response.status_code





api_key = "c8f989abf579c4f0e39a8115159fa9a6100066cd"
net_id = "L_743656888469554260"
show_l3_firewall_block_rules(api_key, net_id)