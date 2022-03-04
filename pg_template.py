from tkinter import Menu
from clear_console import *
from py_to_postgres import *

def pg_template(login):
    obj=database_gateway()
    
    clearConsole()
    print("Welcome to PAK Bank".center(os.get_terminal_size().columns," "))
    print("                     ")
    print("                     Account holder: ",obj.get_name_of_account_owner(login))
    print("                     Status: Logged In")
    print("                     ")
    print("                     ")
    print("                     ")