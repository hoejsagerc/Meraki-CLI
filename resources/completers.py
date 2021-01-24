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

__all__ = ['tier1_completer', 'tier2_completer', 'tier3_completer', 'tier4_completer']

# User Exec Mode
def tier1_completer():
    return ['enable', 'exit', 'help']

# User Enabled Mode
def tier2_completer():
    return ['exit', 'help','select', 'config', 'show', 'run', 'network', 'networks', 'brief', 'show networks brief']

# Global Config Mode
def tier3_completer():
    return ['exit', 
        'help', 
        'set', 
        'new', 
        'do', 
        'brief', 
        'network', 
        'select', 
        'set new network', 
        'do show networks', 
        'do show networks brief', 
        'select network', 
        'do show network switches', 
        'do show network switches brief', 
        'do show network ap',
        'do show network ap brief',
        'do show network mx', 
        'do show network mx brief']


def tier4_completer():
    return ['exit',
    'help',
    'show',
    'interfaces',
    'show  interfaces']