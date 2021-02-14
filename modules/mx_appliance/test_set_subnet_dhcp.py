import pytest
import os
from modules.mx_appliance.set_subnet_dhcp import update_dhcp, format_input, dhcp_handling_option, create_payload, retrive_configured_vlan

class TestSetSubnetDHCP:

    def test_format_input(self):
        assert format_input('set dhcp vlan 501') == '501'
        assert format_input('set dhcp 501') == None