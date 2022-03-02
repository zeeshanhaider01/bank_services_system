from ast import And
from py_to_postgres import *
# from date_time import curnt_time
# from clear_console import *
from pg_template import *

def creat_acount():
    name=input("                     Please enter your Name:")

    while name=="":
        name=input("                     Name should not be empty: ")

    login=input("                     Please enter your login ID:")
    while login=="":
        login=input("                     Enter again (LoginID should not be empty): ")
    
    while check_login_prsnt(login)==True or login=="": #from "py_to_postgres" file, function imported
        while login=="":
            login=input("                     Enter again (LoginID should not be empty): ")

        login=input("                     Login ID already exists please enter a unique ID:")
        while login=="":
            login=input("                     Enter again (LoginID should not be empty): ")

        if check_login_prsnt(login)==True or login=="": #from "py_to_postgres" file, function imported
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
   
    set_new_user_record(login,name,paswrd,balnc=0) #from "py_to_postgres" file, function imported
    pg_template(login)
    
    swill=input("                     Would you like to deposit amount? Y/N: ")
    pg_template(login)
    state=False
    while state==False:
        
        if swill=="Y" or swill=="y" or swill=="N" or swill=="n":
            # state=True
            if swill=="Y" or swill=="y":
                # balnc=input("                     enter the amount: ")
                # print("balnc type: ",type(balnc))
                # input("some thing: ")

                def int_pre(val):
                            for item in val:
                                if item not in ["0","1","2","3","4","5","6","7","8","9"]:
                                    return False
                                
                            return True

                amount=input("                     Please enter the amount: ")
                if int_pre(amount)==False or amount=="":
                # while amount<0:
                #     amount=int(input("                     Please enter positive amount: "))
                    state=True
                    while state==True:
                        amount=input("                     Please enter amount in given format:(123456789): ")
                        if int_pre(amount)==True and amount!="":
                            state=False
                            amount=int(amount)
                        else:
                            pass
                amount=int(amount)
                set_balnc(login,amount) #from "py_to_postgres" file, function imported
                logio="login"
                set_record_login_out(login,logio) #from "py_to_postgres" file, function imported
                pg_template(login)
                will=True
                while will:
                    
                    print("                     Main Menu:")
                    print("                     1-For Checking Account Balance:")
                    print("                     2-For Cash Withdrawal:")
                    print("                     3-For Cash Deposit:")
                    print("                     4-For Logout:")
                    print("                     5-For Account History:")
                    servs=input("                     Press any key:1,2,3,4,5: ")
                    
                    
                    if servs=="1":
                        pg_template(login)

                        val=get_balnc(login)
                        print("                     Your account balance is: ",val," Rs")
                        print("                     *********************************************")
                        val=input("                     For Main Menu: Press(Enter) ")
                        pg_template(login)
                    
                    elif servs=="2":
                        pg_template(login)

                        def int_pre(val):
                            for item in val:
                                if item not in ["0","1","2","3","4","5","6","7","8","9"]:
                                    return False
                                
                            return True

                        amount=input("                     Please enter the amount: ")
                        if int_pre(amount)==False or amount=="":
                        # while amount<0:
                        #     amount=int(input("                     Please enter positive amount: "))
                            state=True
                            while state==True:
                                amount=input("                     Please enter amount in given format:(123456789): ")
                                if int_pre(amount)==True and amount!="":
                                    state=False
                                    amount=int(amount)
                                else:
                                    pass
                        amount=int(amount)
                        if get_balnc(login)>=amount:
                            print("                     Have your Cash: ",amount," Rs")
                            balnc=get_balnc(login)-amount
                            set_balnc(login,balnc)
                            print("                     Your remaining balance is: ",get_balnc(login))

                            trans_typ="debit"
                            set_record_transaction(login,trans_typ,amount)
                            print("                     *********************************************")
                            val=input("                     For Main Menu: Press(Enter) ")
                            pg_template(login)
                        else:
                            print("                     Insufficient amount")
                            print("                     You can withdraw maximum: ",get_balnc(login)," Rs")
                            print("                     *********************************************")
                            val=input("                     For Main Menu: Press(Enter) ")
                            pg_template(login)
                    
                    elif servs=="3":
                        pg_template(login)

                        # amount=input("                     Please enter the amount: ")
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
                        balnc=get_balnc(login)+amount
                        set_balnc(login,balnc)
                        print("                     Your new balance is: ", get_balnc(login))

                        trans_typ="credit"
                        set_record_transaction(login,trans_typ,amount)
                        print("                     *********************************************")
                        val=input("                     For Main Menu: Press(Enter) ")
                        pg_template(login)
                    elif servs=="4":
                        # pg_template(login)

                        # print("                     Logged Out.")

                        logio="logout"
                        set_record_login_out(login,logio)
                        will=False
                        state=True
                    elif servs=="5":
                        pg_template(login)

                        user_history(login)
                        val=input("                     For Main Menu: Press(Enter) ")
                        pg_template(login)

            elif swill=="N" or swill=="n":
                balnc=0
                set_balnc(login,balnc)  #from "py_to_postgres" file, function imported
                logio="login"
                set_record_login_out(login,logio)  #from "py_to_postgres" file, function imported
                will=True
                while will:
                    
                    print("                     Main Menu:")
                    print("                     1-For Checking Account Balance:")
                    print("                     2-For Cash Withdrawal:")
                    print("                     3-For Cash Deposit:")
                    print("                     4-For Logout:")
                    print("                     5-For Account History:")
                    servs=input("                     Press any key:1,2,3,4,5: ")
                    
                    
                    if servs=="1":
                        pg_template(login)

                        val=get_balnc(login)
                        print("                     Your account balance is: ",val," Rs")
                        print("                     *********************************************")
                        val=input("                     For Main Menu: Press(Enter) ")
                        pg_template(login)
                    
                    elif servs=="2":
                        pg_template(login)

                        def int_pre(val):
                            for item in val:
                                if item not in ["0","1","2","3","4","5","6","7","8","9"]:
                                    return False
                            return True

                        amount=input("                     Please enter the amount: ")
                        if int_pre(amount)==False or amount=="":
                        # while amount<0:
                        #     amount=int(input("                     Please enter positive amount: "))
                            state=True
                            while state==True:
                                amount=input("                     Please enter amount in given format:(123456789): ")
                                if int_pre(amount)==True and amount!="":
                                    state=False
                                    amount=int(amount)
                                else:
                                    pass
                        amount=int(amount)
                        if get_balnc(login)>=amount:
                            print("                     Have your Cash: ",amount," Rs")
                            balnc=get_balnc(login)-amount
                            set_balnc(login,balnc)
                            print("                     Your remaining balance is: ",get_balnc(login))

                            trans_typ="debit"
                            set_record_transaction(login,trans_typ,amount)
                            print("                     *********************************************")
                            val=input("                     For Main Menu: Press(Enter) ")
                            pg_template(login)
                        else:
                            print("                     Insufficient amount")
                            print("                     You can withdraw maximum: ",get_balnc(login)," Rs")
                            print("                     *********************************************")
                            val=input("                     For Main Menu: Press(Enter) ")
                            pg_template(login)
                    
                    elif servs=="3":
                        pg_template(login)

                        # amount=input("                     Please enter the amount: ")
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
                        balnc=get_balnc(login)+amount
                        set_balnc(login,balnc)
                        print("                     Your new balance is: ", get_balnc(login))

                        trans_typ="credit"
                        set_record_transaction(login,trans_typ,amount)
                        print("                     *********************************************")
                        val=input("                     For Main Menu: Press(Enter) ")
                        pg_template(login)
                    elif servs=="4":
                        # pg_template(login)

                        # print("                     Logged Out.")

                        logio="logout"
                        set_record_login_out(login,logio)
                        will=False
                        state=True
                    elif servs=="5":
                        pg_template(login)

                        user_history(login)
                        val=input("                     For Main Menu: Press(Enter) ")
                        pg_template(login)
            else:
                pass
        else:
            pg_template(login)
            swill=input("                     Would you like to deposit amount? Y/N: ")  
            # clearConsole()
            # print("Welcome to PAK Bank".center(os.get_terminal_size().columns," "))
            # print("                     ")