import pytest
from modules.mx_appliance.delete_vlan import format_input


def test_format_input():
   assert format_input('delete vlan 501') == '501'