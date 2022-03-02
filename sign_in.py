from py_to_postgres import *
from clear_console import *
from pg_template import *
import getpass
def sign_in():
    login=input("                     Please enter Login: ")
    while check_login_prsnt(login)==False:
        login=input("                     Please enter correct Login: ")
        if check_login_prsnt(login)==False:
            next=input("                     Back to main menu: press(y)")
            if next=="y" or next=="Y":

                pg_template(login)

                return None
    if check_login_prsnt(login)==True:
        # lgin=login
        passwrd=getpass.getpass("                     Please enter your password: ")
        
      
        while check_pswd_prsnt(login,passwrd)==False:
            passwrd=getpass.getpass("                     Please enter correct password: ")
            if check_pswd_prsnt(login,passwrd)==False:
                next=input("                     Back to main menu: press(y)")
                if next=="y" or next=="Y":

                    pg_template(login)

                    return None 
        
        if check_pswd_prsnt(login,passwrd)==True:
            # acount_record[login]["history"].append({curnt_time():"User Loggedin"})
            logio="login"
            set_record_login_out(login,logio)
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
                elif servs=="5":
                    pg_template(login)

                    user_history(login)
                    val=input("                     For Main Menu: Press(Enter) ")
                    pg_template(login)
