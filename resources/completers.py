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

__all__ = ['tier1_completer', 'tier2_completer', 'tier3_completer', 'tier4_completer', 'mx_int_completer']

# User Exec Mode
def tier1_completer():
    return ['enable', 'exit', 'help', 'new user']

# User Enabled Mode
def tier2_completer():
    return ['exit', 'help','show networks brief', 'show networks', 'config terminal', ]

# Global Config Mode
def tier3_completer():
    return ['exit', 
        'help',
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
        'select mx'
    ]



def tier4_completer():
    return ['exit',
        'help',
        'show interfaces',
        'select interfaces'
    ]

def mx_int_completer():
    return ['exit', 
        'help',
        'show interface config',
        'set interface trunk',
        'set interface access'
    ]