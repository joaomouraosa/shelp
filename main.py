import sys
from INFO import INFO


def print_cmd(key):
    cmd = INFO[key]
    _depth_search(cmd, 0)


def _depth_search(cmd, n):
    blanks = ''.join(['  ' for x in range(0, n)])
    if type(cmd) is dict:
        for k in cmd.keys():
            print(f'{blanks}{k}')
            _depth_search(cmd[k], n+1)
    elif type(cmd) is list:
        for l in cmd:
            print(f'{blanks}{l}')
    else:
        print(f'{blanks}{cmd}')


def print_help():
    print("Commands")
    for k in INFO.keys():
        print(f'''\t [{k}] ''')
    print("$ shelp  [command]")


def main():
    try:
        COMMAND = sys.argv[1]
    except IndexError:
        COMMAND = help

    print_help() if (COMMAND == 'help' or COMMAND not in INFO.keys()) else print_cmd(COMMAND)
