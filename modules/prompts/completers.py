"""
    NAME
        completers.py
    CREATED
        23.01.2021
    DESCRIPTION
        This file contains the different word completers for
        the different menus.
    UPDATED
        23.01.2021
"""

__all__ = ['tier1_completer', 'tier2_completer', 'tier3_completer', 'tier4_mx_completer', 'mx_int_completer','mx_int_range_completer', 'tier4_ms_completer', 'ms_int_completer', 'ms_int_range_completer']

# User Exec Mode
def tier1_completer():
    return ['enable', 'exit', 'help', 'new user', 'new', 'user']


# User Enabled Mode
def tier2_completer():
    return ['exit', 
    'help',
    'show networks brief', 
    'show networks', 
    'config terminal', 
    'show all network status', 
    'show network status',
    'test network connection',
    'test',
    'connection',
    'show',
    'networks',
    'network',
    'config',
    'terminal',
    'brief']


# Global Config Mode
def tier3_completer():
    return [
        'select network',
        'set new network',
        'delete network',
        'set new network device',
        'delete network device',
        'set device name',
        'show network switches',
        'show network switches brief',
        'show network ap',
        'show network ap brief',
        'show network mx',
        'show network mx brief',
        'show run ssids',
        'show ssids brief',
        'show enabled ssids',
        'select mx',
        'select switch'
        'exit', 
        'help',
        'select',
        'new',
        'network',
        'delete',
        'device',
        'name',
        'switches',
        'ap',
        'mx',
        'brief'
        'ssids',
        'enabled'
    ]


def tier4_mx_completer():
    return ['exit',
        'help',
        'show interfaces',
        'select interfaces',
        'set dhcp vlan',
        'show dhcp vlan',
        'set firewall rule',
        'show firewall rules',
        'show firewall block rules',
        'show firewall allow rules',
        'delete firewall rule'
        'show',
        'select',
        'interfaces',
        'firewall',
        'rule',
        'rules',
        'block',
        'allow',
        'delete'
    ]


def mx_int_completer():
    return ['exit', 
        'help',
        'show interface config',
        'set interface trunk',
        'set interface access'
        'show',
        'set',
        'interface',
        'config',
        'trunk',
        'access'
    ]


def mx_int_range_completer():
    return ['exit',
        'help',
        'set interface access',
        'set',
        'interface',
        'access']


def tier4_ms_completer():
    return [
        'exit',
        'help'
    ]


def ms_int_completer():
    return [
        'exit',
        'help'
    ]


def ms_int_range_completer():
    return [
        'exit',
        'help'
    ]