from account_record import acount_record #Here we are importing the bank accounts record
from date_time import curnt_time
from clear_console import *
def creat_acount():
    login=input("Please enter your login ID:")
    
    while login in acount_record: #we are importing dictionary called "acount_record from file "account_record"
        login=input("This login ID already exists please enter a unique ID:")
    
    acount_record[login]={}
    paswrd=input("Please enter unique your password: ")
    acount_record[login]["password"]=paswrd
    acount_record[login]["history"]=[]
    # acount_record[login]["history"]["date"]={}

    print("congratulations your account has created.")
    clearConsole()
    
    will=input("Would you like to deposit amount? Y/N: ")
    clearConsole()
    if will=="Y" or will=="y":
        amount=input("enter the amount: ")
        acount_record[login]["balance"]=amount
        acount_record[login]["history"].append({curnt_time():"User Loggedin"})
        will=True
        while will:
            
            print("*********************************************")
            print("1-For Checking Account Balance:")
            print("2-For Cash Withdrawal:")
            print("3-For Cash Deposit:")
            print("4-For Logout:")
            print("5-For Account History:")
            servs=input("Press any key:1,2,3,4,5: ")
            print("*********************************************")
            
            
            if servs=="1":
                clearConsole()
                print("Your account balance is: ",acount_record[login]["balance"]," Rs")
                acount_record[login]["history"].append({curnt_time():"balance checked"})
                print("*********************************************")
            
            elif servs=="2":
                clearConsole()
                amount=input("Please enter the amount: ")
                if int(acount_record[login]["balance"])>=int(amount):
                    print("Have your Cash: ",amount," Rs")
                    acount_record[login]["balance"]=str(int(acount_record[login]["balance"])-int(amount))
                    print("Your remaining balance is: ",acount_record[login]["balance"])
                    
                    acount_record[login]["history"].append({curnt_time():"account debited"})
                    print("*********************************************")
                else:
                    print("Insufficient amount")
                    print("You can withdraw maximum: ",acount_record[login]["balance"]," Rs")
                    
                    acount_record[login]["history"].append({curnt_time():"account was not debited due insufficient funds"})
                    print("*********************************************")
            
            elif servs=="3":
                clearConsole()
                amount=input("Please enter the amount: ")
                acount_record[login]["balance"]=str(int(acount_record[login]["balance"])+int(amount))
                print("Your new balance is: ", acount_record[login]["balance"])
                acount_record[login]["history"].append({curnt_time():"account credited"})
                print("*********************************************")
            elif servs=="4":
                clearConsole()
                print("Logged Out.")
                acount_record[login]["history"].append({curnt_time():"logged out"})
                print_his=input("want to see history:(y/n) ")
                if print_his=="y" or print_his=="Y":
                    for item in acount_record[login]["history"]:
                        print(item)
                will=False
            elif servs=="5":
                clearConsole()
                for item in acount_record[login]["history"]:
                    print(item)
    else:
        acount_record[login]["balance"]="0"
        acount_record[login]["history"].append({curnt_time():"User Loggedin"})
        will=True
        while will:
            clearConsole()
            print("*********************************************")
            print("1-For Checking Account Balance:")
            print("2-For Cash Withdrawal:")
            print("3-For Cash Deposit:")
            print("4-For Logout:")
            print("5-For Account History:")
            servs=input("Press any key:1,2,3,4,5: ")
            print("*********************************************")
            
            
            if servs=="1":
                clearConsole()
                print("Your account balance is: ",acount_record[login]["balance"]," Rs")
                acount_record[login]["history"].append({curnt_time():"balance checked"})
                print("*********************************************")
            
            elif servs=="2":
                clearConsole()
                amount=input("Please enter the amount: ")
                if int(acount_record[login]["balance"])>=int(amount):
                    print("Have your Cash: ",amount," Rs")
                    acount_record[login]["balance"]=str(int(acount_record[login]["balance"])-int(amount))
                    print("Your remaining balance is: ",acount_record[login]["balance"])
                    
                    acount_record[login]["history"].append({curnt_time():"account debited"})
                    print("*********************************************")
                else:
                    print("Insufficient amount")
                    print("You can withdraw maximum: ",acount_record[login]["balance"]," Rs")
                    
                    acount_record[login]["history"].append({curnt_time():"account was not debited due insufficient funds"})
                    print("*********************************************")
            
            elif servs=="3":
                clearConsole()
                amount=input("Please enter the amount: ")
                acount_record[login]["balance"]=str(int(acount_record[login]["balance"])+int(amount))
                print("Your new balance is: ", acount_record[login]["balance"])
                acount_record[login]["history"].append({curnt_time():"account credited"})
                print("*********************************************")
            elif servs=="4":
                clearConsole()
                print("Logged Out.")
                acount_record[login]["history"].append({curnt_time():"logged out"})
                print_his=input("want to see history:(y/n) ")
                if print_his=="y" or print_his=="Y":
                    for item in acount_record[login]["history"]:
                        print(item)
                will=False
            elif servs=="5":
                clearConsole()
                for item in acount_record[login]["history"]:
                    print(item)