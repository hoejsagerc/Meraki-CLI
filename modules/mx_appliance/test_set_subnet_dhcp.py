import pytest
import os
from modules.mx_appliance.set_subnet_dhcp import update_dhcp, format_input, dhcp_handling_option, create_payload, retrive_configured_vlan

class TestSetSubnetDHCP:

    API_KEY = os.getenv('API_KEY')
    NET_ID = os.getenv('NET_ID')

    def test_format_input(self):
        assert format_input('set dhcp vlan 501') == '501'
        assert format_input('set dhcp 501') == None


    def test_dhcp_handling_option1(self):
        dhcp_handling_option.input = lambda: "1"
        dhcp_handling, option = dhcp_handling_option()
        assert dhcp_handling == "Run a DHCP server"
        assert option == "1"

    
    def test_dhcp_handling_option2(self):
        dhcp_handling_option.input = lambda: "2"
        dhcp_handling, option = dhcp_handling_option()
        assert dhcp_handling == "Relay DHCP to another server"
        assert option == "2"

    
    def test_dhcp_handling_option3(self):
        dhcp_handling_option.input = lambda: "3"
        dhcp_handling, option = dhcp_handling_option()
        assert dhcp_handling == "Do not respond to DHCP requests"
        assert option == "3"

    
    def test_dhcp_handling_optionFail(self):
        dhcp_handling_option.input = lambda: "4"
        assert dhcp_handling_option() == None


    def test_retrieve_configured_vlan(self):
        assert retrive_configured_vlan("test", "test", "501") == None