import sys
from termcolor import cprint
from bot.commands.check import run as check
from bot.commands.new import run as new
from bot.commands.update import run as update
from server.app import __main__ as server


def menu():
    cprint("\n Simple Trading Bot -  \n", attrs=["bold"])
    cprint(f"--check    -c \t Check config \n")
    cprint(f"--new      -n \t Start new cycle \n")
    cprint(f"--update   -u \t Update running cycles \n")
    cprint(f"--server   -s \t Update running cycles \n")


if __name__ == '__main__':
    argv = sys.argv
    if "--check" in argv or "-c" in argv:
        check()
    elif "--new" in argv or "-n" in argv:
        new()
    elif "--update" in argv or "-u" in argv:
        update()
    elif "--server" in argv or "-s" in argv:
        server()
    else:
        menu()
