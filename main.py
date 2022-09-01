import sys
from INFO import INFO


def print_cmd(cmd):
    for k in INFO[cmd].keys():
        print(k)
        for l in INFO[cmd][k]:
            print('\t' + l)


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


