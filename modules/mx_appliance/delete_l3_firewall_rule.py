import json
import requests

__all__ = ['remove_l3_firewall_rule']


def retrieve_rules(api_key, net_id):

    url = "https://api.meraki.com/api/v1/networks/{}/appliance/firewall/l3FirewallRules".format(net_id)

    payload = None

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "X-Cisco-Meraki-API-Key": api_key
    }
    
    response = requests.request('GET', url, headers=headers, data = payload)

    return response.json()


def create_new_rule_object(api_key, net_id, rule_number):

    rule_object = retrieve_rules(api_key, net_id)

    for i in range(len(rule_object['rules'])):
        if rule_object['rules'][i] == rule_object['rules'][rule_number]:
            del rule_object['rules'][i]
            break
    
    for i in range(len(rule_object['rules'])):
        if rule_object['rules'][i]['comment'] == "Default rule":
            del rule_object['rules'][i]
            break
    
    return dict(rule_object)


def format_input(usr_input):
    if len(usr_input.split()) == 4:
        try:
            output = (usr_input.split())[3]
            return output
        except:
            return None
    else:
        return None


def remove_l3_firewall_rule(api_key, net_id, rule_number):

    url = "https://api.meraki.com/api/v1/networks/{}/appliance/firewall/l3FirewallRules".format(net_id)

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "X-Cisco-Meraki-API-Key": api_key
    }
    rule_number = int(format_input(rule_number))

    usr_action = input(f"Are you sure you want to remove firewall rule: {rule_number} - (y/n): ")

    if usr_action == "y" or usr_action == "Y":

        payload = create_new_rule_object(api_key, net_id, rule_number)

        try:
            response = requests.request('PUT', url, headers=headers, data = json.dumps(payload))

        except:
            print("Couldn't complete command, make sure you are typing correct...")

        if response.status_code == 200:
            print("Successfully removed firewall rule")
            print(json.dumps(payload, indent=4, sort_keys=True))
            return response
        else:
            print("An error occured, couldn't remove the firewall rule")
            return response
    
    else:
        pass


