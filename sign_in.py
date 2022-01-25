from account_record import acount_record
from date_time import curnt_time
from clear_console import *
def sign_in():
    login=input("Please enter Login: ")
    while login not in acount_record:
        login=input("Please enter correct Login: ")
        if login not in acount_record:
            next=input("Back to main menu: press(y)")
            if next=="y" or next=="Y":
                clearConsole()
                return None
    if login in acount_record:
        lgin=login
        password=input("Please enter your password: ")
        clearConsole()
        while acount_record[lgin]["password"]!=password:
            password=input("Please enter your correct password: ")
            if password not in acount_record[lgin]:
                next=input("Back to main menu: press(y)")
                if next=="y" or next=="Y":
                    clearConsole()
                    return None 
        
        if acount_record[lgin]["password"]==password:
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
                    print("Your account balance is: ",acount_record[lgin]["balance"]," Rs")
                    acount_record[login]["history"].append({curnt_time():"balance checked"})
                    print("*********************************************")
                
                elif servs=="2":
                    clearConsole()
                    amount=input("Please enter the amount: ")
                    if int(acount_record[lgin]["balance"])>=int(amount):
                        print("Have your Cash: ",amount," Rs")
                        acount_record[lgin]["balance"]=str(int(acount_record[lgin]["balance"])-int(amount))
                        print("Your remaining balance is: ",acount_record[lgin]["balance"])
                        
                        acount_record[login]["history"].append({curnt_time():"account debited"})
                        print("*********************************************")
                    else:
                        print("Insufficient amount")
                        print("You can withdraw maximum: ",acount_record[lgin]["balance"]," Rs")
                      
                        acount_record[login]["history"].append({curnt_time():"account was not debited due insufficient funds"})
                        print("*********************************************")
                
                elif servs=="3":
                    clearConsole()
                    amount=input("Please enter the amount: ")
                    acount_record[lgin]["balance"]=str(int(acount_record[lgin]["balance"])+int(amount))
                    print("Your new balance is: ", acount_record[lgin]["balance"])
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
