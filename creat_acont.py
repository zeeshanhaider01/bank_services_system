from ast import And
from py_to_postgres import *
# from date_time import curnt_time
# from clear_console import *
from pg_template import *
from Login_menu import menu


def creat_acount():
    obj=database_gateway()
    name=input("                     Please enter your Name:")

    while name=="":
        name=input("                     Name should not be empty: ")

    login=input("                     Please enter your login ID:")
    while login=="":
        login=input("                     Enter again (LoginID should not be empty): ")
    
    while obj.check_login_prsnt(login)==True or login=="": #from "py_to_postgres" file, function imported
        while login=="":
            login=input("                     Enter again (LoginID should not be empty): ")

        login=input("                     Login ID already exists please enter a unique ID:")
        while login=="":
            login=input("                     Enter again (LoginID should not be empty): ")

        if obj.check_login_prsnt(login)==True or login=="": #from "py_to_postgres" file, function imported
            next=input("                     Back to main menu: press(Y) or (enter) else  press any other key to continue: ")
            
            if next=="y" or next=="Y" or next=="":

                clearConsole()
                print("Welcome to PAK Bank".center(os.get_terminal_size().columns," "))
                print("                     ")

                return None
            else:
                login=input("                     Please enter a unique Login ID:")
    
   
    paswrd=input("                     Please enter your password: ")
    while paswrd=="":
        paswrd=input("                     Enter again (Password should not be empty): ")
   
    obj.set_new_user_record(login,name,paswrd,balnc=0) #from "py_to_postgres" file, function imported
    pg_template(login)
    
    swill=input("                     Would you like to deposit amount? Y/N: ")
    pg_template(login)
    state=False
    while state==False:
        
        if swill=="Y" or swill=="y" or swill=="N" or swill=="n":
            # state=True
            if swill=="Y" or swill=="y":
                def int_pre(val):
                    for item in val:
                        if item not in ["0","1","2","3","4","5","6","7","8","9"]:
                            return False  
                    return True

                amount=input("                     Please enter the amount: ")
                if int_pre(amount)==False or amount=="":
                    state=True
                    while state==True:
                        amount=input("                     Please enter amount in given format:(123456789): ")
                        if int_pre(amount)==True and amount!="":
                            state=False
                            amount=int(amount)
                        else:
                            pass
                amount=int(amount)
                obj.set_balnc(login,amount) #from "py_to_postgres" file, function imported
                logio="login"
                obj.set_record_login_out(login,logio) #from "py_to_postgres" file, function imported
                
                pg_template(login)
                objtwo=menu()
                objtwo.mainmenu(login)
                state=True

            elif swill=="N" or swill=="n":
                balnc=0
                obj.set_balnc(login,balnc)  #from "py_to_postgres" file, function imported
                logio="login"
                obj.set_record_login_out(login,logio)  #from "py_to_postgres" file, function imported
                objtwo=menu()
                objtwo.mainmenu(login)
                state=True
            else:
                pass
        else:
            pg_template(login)
            swill=input("                     Would you like to deposit amount? Y/N: ")  
            # clearConsole()
            # print("Welcome to PAK Bank".center(os.get_terminal_size().columns," "))
            # print("                     ")