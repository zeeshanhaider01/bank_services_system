from py_to_postgres import *
from date_time import curnt_time
from clear_console import *
import getpass
def sign_in():
    login=input("                     Please enter Login: ")
    while check_login_prsnt(login)==False:
        login=input("                     Please enter correct Login: ")
        if check_login_prsnt(login)==False:
            next=input("                     Back to main menu: press(y)")
            if next=="y" or next=="Y":
                clearConsole()
                print("Welcome to PAK Bank".center(os.get_terminal_size().columns," "))
                print("                     ")
                return None
    if check_login_prsnt(login)==True:
        # lgin=login
        passwrd=getpass.getpass("                     Please enter your password: ")
        
      
        while check_pswd_prsnt(login,passwrd)==False:
            password=input("                     Please enter your correct password: ")
            if check_pswd_prsnt(login,passwrd)==False:
                next=input("                     Back to main menu: press(y)")
                if next=="y" or next=="Y":
                    clearConsole()
                    print("Welcome to PAK Bank".center(os.get_terminal_size().columns," "))
                    print("                     ")
                    return None 
        
        if check_pswd_prsnt(login,passwrd)==True:
            # acount_record[login]["history"].append({curnt_time():"User Loggedin"})
            logio="login"
            set_record_login_out(login,logio)
            will=True
            while will:
                print("                     Account holder: ",get_name_of_account_owner(login))
                print("                     *********************************************")
                print("                     1-For Checking Account Balance:")
                print("                     2-For Cash Withdrawal:")
                print("                     3-For Cash Deposit:")
                print("                     4-For Logout:")
                print("                     5-For Account History:")
                servs=input("                     Press any key:1,2,3,4,5: ")
                print("                     *********************************************")
                
                
                if servs=="1":
                    clearConsole()
                    print("Welcome to PAK Bank".center(os.get_terminal_size().columns," "))
                    print("                     ")
                    val=get_balnc(login)
                    print("                     Your account balance is: ",val," Rs")
                    # acount_record[login]["history"].append({curnt_time():"balance checked"})
                    print("                     *********************************************")
                
                elif servs=="2":
                    clearConsole()
                    print("Welcome to PAK Bank".center(os.get_terminal_size().columns," "))
                    print("                     ")

                    amount=input("                     Please enter the amount: ")
                    if int(get_balnc(login))>=int(amount):
                        # print("                     Have your Cash: ",amount," Rs")
                        balnc=int(get_balnc(login))-int(amount)
                        set_balnc(login,balnc)
                        print("                     Your remaining balance is: ",get_balnc(login))

                        trans_typ="debit"
                        set_record_transaction(login,trans_typ,amount)
                        
                        # acount_record[login]["history"].append({curnt_time():"account debited"})
                        print("                     *********************************************")
                    else:
                        print("                     Insufficient amount")
                        print("                     You can withdraw maximum: ",get_balnc(login)," Rs")
                        
                        # acount_record[login]["history"].append({curnt_time():"account was not debited due insufficient funds"})
                        print("                     *********************************************")
                
                elif servs=="3":
                    clearConsole()
                    print("Welcome to PAK Bank".center(os.get_terminal_size().columns," "))
                    print("                     ")

                    amount=input("                     Please enter the amount: ")
                    balnc=get_balnc(login)+int(amount)
                    set_balnc(login,balnc)
                    print("                     Your new balance is: ", get_balnc(login))

                    trans_typ="credit"
                    set_record_transaction(login,trans_typ,amount)
                    # acount_record[login]["history"].append({curnt_time():"account credited"})
                    print("                     *********************************************")
                elif servs=="4":
                    clearConsole()
                    print("Welcome to PAK Bank".center(os.get_terminal_size().columns," "))
                    print("                     ")

                    print("                     Logged Out.")

                    logio="logout"
                    set_record_login_out(login,logio)
                    # acount_record[login]["history"].append({curnt_time():"logged out"})
                    # json_write() # Before loggout this function stores all the data of the user to file for permanent storage
                    will=False
                elif servs=="5":
                    clearConsole()
                    print("Welcome to PAK Bank".center(os.get_terminal_size().columns," "))
                    print("                     ")
                    user_history(login)
