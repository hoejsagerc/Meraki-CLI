import json
import requests

__all__ = ["create_new_ssid"]


def format_input(usr_input):
    if len(usr_input.split()) == 4:
        try:
            output = (usr_input.split())[3]
            return output
        except:
            return None
    else:
        return None


def create_radius_payload(ssid_number, auth_mode):
    print("Press Enter for default answers marked by [xxx].")
    name  = input("Enter name of the SSID: ")
    enabled = input("Enter ['true'] for enabling the ssid, or enter 'false' for disabling the ssid: ")
    if enabled == "":
        enabled = "true"
    vlan_id = input("Enter the vlan id: ")
    visible = input("Enter ['true'] if ssid should be visible, or 'false' if it should be hidden: ")
    if visible == "":
        visible = "true"
    radius_server = input("Enter the ip address of your radius server: ")
    radius_port = input("Enter the UDP port the radius server listens on: ")
    radius_secret = input("Enter the client shared secret for the radius server: ")
    radius_failover_pol = input("Enter the failover-policy ['Deny access'] or 'Allow access': ")
    if radius_failover_pol == "":
        radius_failover_pol = "Deny access"
    print("Types of splash pages: ['None'], 'Click-through splash page',")
    splash_page = input("Enter the type of splash page: ")
    if splash_page == "":
        splash_page = "None"
    print("Types of ip assignment modes: 'NAT mode', ['Bridge mode'], Layer 3 roaming', 'Layer 3 roaming with a conentrator'")
    ip_assignment = input("Enter the ip assignment mode: ")
    if ip_assignment == "":
        ip_assignment = "Bridge mode"
    print("Band selections: ['Dual band operation'], '5 GHz band only', 'Dual band operation with Band Steering'")
    band_selection = input("Enter the band selection: ")
    if band_selection == "":
        band_selection = "Dual band operation"

    payload = {
        "number": ssid_number,
        "name": name,
        "enabled": enabled,
        "authMode": auth_mode,
        "defaultVlanId": vlan_id,
        "useVlanTagging": "true",
        "visible": visible,
        "radiusServers": [
            {
                "port": radius_port,
                "host": radius_server,
                "secret": radius_secret
            }
        ],
        "radiusFailoverPolicy": radius_failover_pol,
        "ipAssignmentMode": ip_assignment,
        "splashPage": splash_page,
        "splashTimout": "30 minutes",
        "bandSelection": band_selection
    }

    return dict(payload)


def create_open_payload(ssid_number, auth_mode):
    print("Press Enter for default answers marked by [xxx].")
    name  = input("Enter name of the SSID: ")
    enabled = input("Enter ['true'] for enabling the ssid, or enter 'false' for disabling the ssid: ")
    if enabled == "":
        enabled = "true"
    vlan_id = input("Enter the vlan id: ")
    visible = input("Enter ['true'] if ssid should be visible, or 'false' if it should be hidden: ")
    if visible == "":
        visible = "true"
    print("Types of ip assignment modes: 'NAT mode', ['Bridge mode'], Layer 3 roaming', 'Layer 3 roaming with a conentrator'")
    ip_assignment = input("Enter the ip assignment mode: ")
    if ip_assignment == "":
        ip_assignment = "Bridge mode"
    print("Types of splash pages: ['None'], 'Click-through splash page',")
    splash_page = input("Enter the type of splash page: ")
    if splash_page == "":
        splash_page = "None"
    print("Band selections: ['Dual band operation'], '5 GHz band only', 'Dual band operation with Band Steering'")
    band_selection = input("Enter the band selection: ")
    if band_selection == "":
        band_selection = "Dual band operation"

    payload = {
        "number": ssid_number,
        "name": name,
        "enabled": enabled,
        "authMode": auth_mode,
        "defaultVlanId": vlan_id,
        "useVlanTagging": "true",
        "visible": visible,
        "ipAssignmentMode": ip_assignment,
        "splashPage": splash_page,
        "splashTimout": "30 minutes",
        "bandSelection": band_selection
    }

    return dict(payload)


def create_psk_payload(ssid_number, auth_mode):
    print("Press Enter for default answers marked by [xxx].")
    name  = input("Enter name of the SSID: ")
    enabled = input("Enter ['true'] for enabling the ssid, or enter 'false' for disabling the ssid: ")
    if enabled == "":
        enabled = "true"
    vlan_id = input("Enter the vlan id: ")
    visible = input("Enter ['true'] if ssid should be visible, or 'false' if it should be hidden: ")
    if visible == "":
        visible = "true"
    print("Types of ip assignment modes: 'NAT mode', ['Bridge mode'], Layer 3 roaming', 'Layer 3 roaming with a conentrator'")
    ip_assignment = input("Enter the ip assignment mode: ")
    if ip_assignment == "":
        ip_assignment = "Bridge mode"
    encryption_mode = input("Enter 'wep' or ['wpa'] to choose the desired encryption: ")
    if encryption_mode == "":
        encryption_mode = "wpa"

    if encryption_mode == "wpa":
        print("Enter one of the following WPA encryptions: 'WPA1 only', 'WPA1 and WPA2', ['WPA2 only'], WPA3 Transition Mode', WPA3 only'")
        wpa_encryption = input("Enter WPA encryption: ")
        if wpa_encryption == "":
            wpa_encryption = "WPA2 only"
        psk = input("Enter password to authenticate to SSID: ")
    else: 
        wpa_encryption = "{}"
        psk = "{}"

    print("Types of splash pages: ['None'], 'Click-through splash page',")
    splash_page = input("Enter the type of splash page: ")
    if splash_page == "":
        splash_page = "None"
    print("Band selections: ['Dual band operation'], '5 GHz band only', 'Dual band operation with Band Steering'")
    band_selection = input("Enter the band selection: ")
    if band_selection == "":
        band_selection = "Dual band operation"
    
    if encryption_mode == "wpa":
        payload = {
            "number": ssid_number,
            "name": name,
            "enabled": enabled,
            "defaultVlanId": vlan_id,
            "authMode": auth_mode,
            "useVlanTagging": "true",
            "visible": visible,
            "ipAssignmentMode": ip_assignment,
            "encryptionMode": encryption_mode,
            "wpaEncryptionMode": wpa_encryption,
            "psk": psk,
            "splashPage": splash_page,
            "splashTimout": "30 minutes",
            "bandSelection": band_selection
        }
    
    elif encryption_mode == "wep":
        payload = {
            "number": ssid_number,
            "name": name,
            "enabled": enabled,
            "defaultVlanId": vlan_id,
            "authMode": auth_mode,
            "useVlanTagging": "true",
            "visible": visible,
            "ipAssignmentMode": ip_assignment,
            "encryptionMode": encryption_mode,
            "splashPage": splash_page,
            "splashTimout": "30 minutes",
            "bandSelection": band_selection
        }

    return dict(payload)


def create_new_ssid(api_key, net_id, usr_input):

    ssid_number = int(format_input(usr_input))

    auth_mode = input("Enter one of the following Authentication modes: 'open', 'psk' or 8021x-radius: ")
    if auth_mode.lower() == "open":
        payload = create_open_payload(ssid_number, auth_mode)
    
    elif auth_mode.lower() == "psk":
        payload = create_psk_payload(ssid_number, auth_mode)

    elif auth_mode.lower() == "8021x-radius":
        payload = create_radius_payload(ssid_number, auth_mode)

    url = "https://api.meraki.com/api/v1/networks/{}/wireless/ssids/{}".format(net_id, ssid_number)


    print(json.dumps(payload, indent=4, sort_keys=True))

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "X-Cisco-Meraki-API-Key": api_key
    }
    try:
        response = requests.request('PUT', url, headers=headers, data = json.dumps(payload))
    
    except:
        print("Couldn't create the new SSID...")

    if response.status_code == 200:
        print("SSID was sucessfully created!")
        return response.status_code
    
    else:
        print("An error occured, couldn't create the SSID...")
        return response.status_code