from clear_console import *
from py_to_postgres import get_name_of_account_owner

def pg_template(login):

    clearConsole()
    print("Welcome to PAK Bank".center(os.get_terminal_size().columns," "))
    print("                     ")
    print("                     Account holder: ",get_name_of_account_owner(login))
    print("                     Status: Logged In")
    print("                     ")
    print("                     ")
    print("                     ")