import sys
from termcolor import colored, cprint
from bot.commands.check import run as check
from bot.commands.new import run as new


def menu():
    cprint("\n Simple Trading Bot -  \n", attrs=["bold"])
    cprint(f"--check    -c \t Check config \n")
    cprint(f"--new      -n \t Start new cycle \n")
    cprint(f"--update   -u \t Update running cycles \n")


if __name__ == '__main__':
    argv = sys.argv
    if "--check" in argv or "-c" in argv:
        check()
    elif "--new" in argv or "-n" in argv:
        new()
    else:
        menu()
