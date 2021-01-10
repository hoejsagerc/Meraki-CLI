
#* Simple CMD Tool
"""
from prompt_toolkit import prompt

while 1:
    user_input = prompt('>')
    print(user_input)
"""



#* With CMD History
"""
from prompt_toolkit import prompt
from prompt_toolkit.history import FileHistory

while 1:
    user_input = prompt('>',
        history=FileHistory('history.txt'),
    )
    print(user_input)
"""

#* With CMD AutoSuggestions
"""
from prompt_toolkit import prompt
from prompt_toolkit.history import FileHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory

while 1:
    user_input = prompt('>',
        history=FileHistory('history.txt'),
        auto_suggest=AutoSuggestFromHistory(),
    )
    print(user_input)
"""

#* With AutoComplete
from prompt_toolkit import prompt
from prompt_toolkit.history import FileHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.completion import WordCompleter

SQLCompleter = WordCompleter(['select', 'from', 'insert', 'update', 'delete', 'drop'],
    ignore_case=True)

while 1:
    user_input = prompt('SQL>',
        history=FileHistory('history.txt'),
        auto_suggest=AutoSuggestFromHistory(),
        completer=SQLCompleter,
    )
    print(user_input)
