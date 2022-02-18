from account_record import *
#Here we are importing the bank accounts record
from date_time import curnt_time
from clear_console import *
def creat_acount():
    login=input("                     Please enter your login ID:")
    
    while login in acount_record: #we are importing dictionary called "acount_record from file "account_record"
        login=input("                     This login ID already exists please enter a unique ID:")
        if login in acount_record:
            next=input("                     Back to main menu: press(y)")
            if next=="y" or next=="Y":
                clearConsole()
                print("Welcome to PAK Bank".center(os.get_terminal_size().columns," "))
                print("                     ")
                return None
            else:
                login=input("                     please enter a unique ID:")
    
    acount_record[login]={}
    paswrd=input("                     Please enter your password: ")
    acount_record[login]["password"]=paswrd
    acount_record[login]["history"]=[]
    # acount_record[login]["history"]["date"]={}

    print("                     congratulations your account has created.")
    clearConsole()
    print("Welcome to PAK Bank".center(os.get_terminal_size().columns," "))
    print("                     ")
    
    will=input("                     Would you like to deposit amount? Y/N: ")
    clearConsole()
    print("Welcome to PAK Bank".center(os.get_terminal_size().columns," "))
    print("                     ")
    if will=="Y" or will=="y":
        amount=input("                     enter the amount: ")
        acount_record[login]["balance"]=amount
        acount_record[login]["history"].append({curnt_time():"User Loggedin"})
        will=True
        while will:
            
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
                print("                     Your account balance is: ",acount_record[login]["balance"]," Rs")
                acount_record[login]["history"].append({curnt_time():"balance checked"})
                print("                     *********************************************")
            
            elif servs=="2":
                clearConsole()
                print("Welcome to PAK Bank".center(os.get_terminal_size().columns," "))
                print("                     ")

                amount=input("                     Please enter the amount: ")
                if int(acount_record[login]["balance"])>=int(amount):
                    print("                     Have your Cash: ",amount," Rs")
                    acount_record[login]["balance"]=str(int(acount_record[login]["balance"])-int(amount))
                    print("                     Your remaining balance is: ",acount_record[login]["balance"])
                    
                    acount_record[login]["history"].append({curnt_time():"account debited"})
                    print("                     *********************************************")
                else:
                    print("                     Insufficient amount")
                    print("                     You can withdraw maximum: ",acount_record[login]["balance"]," Rs")
                    
                    acount_record[login]["history"].append({curnt_time():"account was not debited due insufficient funds"})
                    print("                     *********************************************")
            
            elif servs=="3":
                clearConsole()
                print("Welcome to PAK Bank".center(os.get_terminal_size().columns," "))
                print("                     ")

                amount=input("                     Please enter the amount: ")
                acount_record[login]["balance"]=str(int(acount_record[login]["balance"])+int(amount))
                print("                     Your new balance is: ", acount_record[login]["balance"])
                acount_record[login]["history"].append({curnt_time():"account credited"})
                print("                     *********************************************")
            elif servs=="4":
                clearConsole()
                print("Welcome to PAK Bank".center(os.get_terminal_size().columns," "))
                print("                     ")

                print("                     Logged Out.")
                acount_record[login]["history"].append({curnt_time():"logged out"})
                json_write() # Before loggout this function stores all the data of the user to file for permanent storage
                will=False
            elif servs=="5":
                clearConsole()
                print("Welcome to PAK Bank".center(os.get_terminal_size().columns," "))
                print("                     ")

                for item in acount_record[login]["history"]:
                    print("                     ",item)
    else:
        acount_record[login]["balance"]="0"
        acount_record[login]["history"].append({curnt_time():"User Loggedin"})
        will=True
        while will:
            # clearConsole()
            # print("Welcome to PAK Bank".center(os.get_terminal_size().columns," "))
            # print("                     ")

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

                print("                     Your account balance is: ",acount_record[login]["balance"]," Rs")
                acount_record[login]["history"].append({curnt_time():"balance checked"})
                print("                     *********************************************")
            
            elif servs=="2":
                clearConsole()
                print("Welcome to PAK Bank".center(os.get_terminal_size().columns," "))
                print("                     ")

                amount=input("                     Please enter the amount: ")
                if int(acount_record[login]["balance"])>=int(amount):
                    print("                     Have your Cash: ",amount," Rs")
                    acount_record[login]["balance"]=str(int(acount_record[login]["balance"])-int(amount))
                    print("                     Your remaining balance is: ",acount_record[login]["balance"])
                    
                    acount_record[login]["history"].append({curnt_time():"account debited"})
                    print("                     *********************************************")
                else:
                    print("                     Insufficient amount")
                    print("                     You can withdraw maximum: ",acount_record[login]["balance"]," Rs")
                    
                    acount_record[login]["history"].append({curnt_time():"account was not debited due insufficient funds"})
                    print("                     *********************************************")
            
            elif servs=="3":
                clearConsole()
                print("Welcome to PAK Bank".center(os.get_terminal_size().columns," "))
                print("                     ")

                amount=input("                     Please enter the amount: ")
                acount_record[login]["balance"]=str(int(acount_record[login]["balance"])+int(amount))
                print("                     Your new balance is: ", acount_record[login]["balance"])
                acount_record[login]["history"].append({curnt_time():"account credited"})
                print("                     *********************************************")
            elif servs=="4":
                clearConsole()
                print("Welcome to PAK Bank".center(os.get_terminal_size().columns," "))
                print("                     ")

                print("                     Logged Out.")
                acount_record[login]["history"].append({curnt_time():"logged out"})
                json_write() # Before loggout this function stores all the data of the user to file for permanent storage
                
                will=False
            elif servs=="5":
                clearConsole()
                print("Welcome to PAK Bank".center(os.get_terminal_size().columns," "))
                print("                     ")

                for item in acount_record[login]["history"]:
                    print("                     ",item)