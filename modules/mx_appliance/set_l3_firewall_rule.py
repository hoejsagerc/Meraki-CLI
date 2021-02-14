import json
import requests

__all__ = ['set_l3_firewall_rule']


def retrieve_firewall_rules(api_key, net_id):
    url = "https://api.meraki.com/api/v1/networks/{}/appliance/firewall/l3FirewallRules".format(net_id)

    payload = None

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "X-Cisco-Meraki-API-Key": api_key
    }

    response = requests.request('GET', url, headers=headers, data = payload)

    return response.json()


def edit_rules(api_key, net_id):

    # old ruleset
    rule_object = retrieve_firewall_rules(api_key, net_id)

    # new rule
    name = input("Enter a descriptive name of the Rule: ")
    policy = input("Enter wether traffic should be 'allowed' or 'deny': ")
    protocol = input("Enter either: 'udp', 'tcp' or 'any': ")

    if protocol != "any":
        src_port = input("Enter the source port: ")
        dest_port = input("Enter the destination port: ")

    src_address = input("Enter the source address as CIDR: ")
    dest_address = input("Enter the destination address as CIDR: ")
    syslog_enabled = input("Enter 'true' to enable syslogging of this rule, or enter 'false' to disable: ")
    rule_number = input("Enter what number the rule should be: ")
    if rule_number == "":
        rule_number == 0

    if protocol != "any":
        payload = {
            "comment": name,
            "policy": policy,
            "protocol": protocol,
            "destPort": dest_port,
            "destCidr": dest_address,
            "srcPort": src_port,
            "srcCidr": src_address,
            "syslogEnabled": syslog_enabled
        }
    else:
        payload = {
            "comment": name,
            "policy": policy,
            "protocol": protocol,
            "destCidr": dest_address,
            "srcCidr": src_address,
            "syslogEnabled": syslog_enabled
        }

    rule_object['rules'].insert(int(rule_number), payload)
    try:
        for i in range(len(rule_object['rules'])):
            if rule_object['rules'][i]['comment'] == "Default rule":
                del rule_object['rules'][i]
            break

        return dict(rule_object)

    except:
        print("An error occured, couldn't create the firewall rule...")    
    



def set_l3_firewall_rule(api_key, net_id):

    url = "https://api.meraki.com/api/v1/networks/{}/appliance/firewall/l3FirewallRules".format(net_id)

    payload = edit_rules(api_key, net_id)

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "X-Cisco-Meraki-API-Key": api_key
    }

    try:
        response = requests.request('PUT', url, headers=headers, data = json.dumps(payload))

    except:
        print("Couldn't complete command, make sure you are typing correct...")

    if response.status_code == 200:
        print("Successfully configured firewall rule")
        print(json.dumps(payload, indent=4, sort_keys=True))
        return response
    else:
        print("An error occured, couldn't configure the firewall rule")
        return response



#api_key = "c8f989abf579c4f0e39a8115159fa9a6100066cd"
#net_id = "L_743656888469554260"
#set_l3_firewall_rule(api_key, net_id)