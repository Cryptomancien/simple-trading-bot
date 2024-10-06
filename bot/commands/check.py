import os.path
import termcolor
from services.database import db


def run():
    # check .env
    path = ".env"
    check_file = os.path.isfile(path)
    if check_file:
        termcolor.cprint(".env found", color="green")
    else:
        termcolor.cprint(".env not found", color="red")
        exit()

    # check api keys
    file = open(path, "r")
    file_content = file.read()
    if "API_PUBLIC" in file_content and "API_SECRET" in file_content:
        termcolor.cprint("API_PUBLIC and API_SECRET found in .env", color="green")
    else:
        termcolor.cprint("API_PUBLIC and API_SECRET not found in .env", color="red")
        exit()

    # check database
    ping = db.database.command("ping")
    if "ok" in ping:
        termcolor.cprint("database ok", color="green")
    else:
        termcolor.cprint("database not found", color="red")
        exit()
