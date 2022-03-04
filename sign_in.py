from py_to_postgres import *
from clear_console import *
from pg_template import *
from Login_menu import menu
import getpass

class signin:

    def signinfunc(self):
        login=input("                     Please enter Login: ")

        obj=database_gateway()

        while obj.check_login_prsnt(login)==False:
            login=input("                     Please enter correct Login: ")
            if obj.check_login_prsnt(login)==False:
                next=input("                     Back to main menu: press(y)")
                if next=="y" or next=="Y":

                    pg_template(login)

                    return None
        if obj.check_login_prsnt(login)==True:
            # lgin=login
            passwrd=getpass.getpass("                     Please enter your password: ")
            
        
            while obj.check_pswd_prsnt(login,passwrd)==False:
                passwrd=getpass.getpass("                     Please enter correct password: ")
                if obj.check_pswd_prsnt(login,passwrd)==False:
                    next=input("                     Back to main menu: press(y)")
                    if next=="y" or next=="Y":

                        pg_template(login)

                        return None 
            
            if obj.check_pswd_prsnt(login,passwrd)==True:
                # acount_record[login]["history"].append({curnt_time():"User Loggedin"})
                logio="login"
                obj.set_record_login_out(login,logio)
                pg_template(login)
                objtwo=menu()
                objtwo.mainmenu(login)
                
