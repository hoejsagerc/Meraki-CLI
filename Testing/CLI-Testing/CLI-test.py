#* With AutoComplete
from prompt_toolkit import prompt
from prompt_toolkit.history import FileHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.completion import WordCompleter


def main_loop():
    while 1:
        t1_completer = WordCompleter(['enable', 'exit'], ignore_case=True)
        user_input = prompt('>', history=FileHistory('history.txt'), auto_suggest=AutoSuggestFromHistory(), completer=t1_completer,)
        print(user_input)


if __name__ == '__main__':

    try:
        main_loop()
    except KeyboardInterrupt:
        print >> sys.stderr, '\nExiting by user request.\n'
        sys.exit(0)
 

