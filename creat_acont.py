from py_to_postgres import *
#Here we are importing the bank accounts record
from date_time import curnt_time
from clear_console import *
def creat_acount():
    name=input("                     Please enter your Name:")
    login=input("                     Please enter your login ID:")
    
    while check_login_prsnt(login)==True: #we are importing dictionary called "acount_record from file "account_record"
        login=input("                     This login ID already exists please enter a unique ID:")
        if check_login_prsnt(login)==True:
            next=input("                     Back to main menu: press(y)")
            if next=="y" or next=="Y":
                clearConsole()
                print("Welcome to PAK Bank".center(os.get_terminal_size().columns," "))
                print("                     ")
                return None
            else:
                login=input("                     please enter a unique ID:")
    
    # acount_record[login]={}
    paswrd=input("                     Please enter your password: ")
    # acount_record[login]["password"]=paswrd
    # acount_record[login]["history"]=[]
    # acount_record[login]["history"]["date"]={}

    # print("                     congratulations your account has created.")
    
    # set_balnc(login,balance=0)
    # set_record_login_out(login,logio)
    clearConsole()
    print("Welcome to PAK Bank".center(os.get_terminal_size().columns," "))
    print("                     ")
    
    will=input("                     Would you like to deposit amount? Y/N: ")
    clearConsole()
    print("Welcome to PAK Bank".center(os.get_terminal_size().columns," "))
    print("                     ")
    if will=="Y" or will=="y":
        balnc=input("                     enter the amount: ")
        set_new_user_record(login,name,paswrd,balnc)
        logio="login"
        set_record_login_out(login,logio)
        # acount_record[login]["balance"]=amount
        # acount_record[login]["history"].append({curnt_time():"User Loggedin"})
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
    else:
        # acount_record[login]["balance"]="0"
        # acount_record[login]["history"].append({curnt_time():"User Loggedin"})
        balnc=0
        set_new_user_record(login,name,paswrd,balnc)
        logio="login"
        set_record_login_out(login,logio)
        will=True
        while will:
            # clearConsole()
            # print("Welcome to PAK Bank".center(os.get_terminal_size().columns," "))
            # print("                     ")
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