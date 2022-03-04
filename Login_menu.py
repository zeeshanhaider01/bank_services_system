from pg_template import *
from py_to_postgres import *
class menu:
    def mainmenu(self,login):
        obj=database_gateway()
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

                val=obj.get_balnc(login)
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
                if obj.get_balnc(login)>=amount:
                    print("                     Have your Cash: ",amount," Rs")
                    balnc=obj.get_balnc(login)-amount
                    obj.set_balnc(login,balnc)
                    print("                     Your remaining balance is: ",obj.get_balnc(login))

                    trans_typ="debit"
                    obj.set_record_transaction(login,trans_typ,amount)
                    print("                     *********************************************")
                    val=input("                     For Main Menu: Press(Enter) ")
                    pg_template(login)
                else:
                    print("                     Insufficient amount")
                    print("                     You can withdraw maximum: ",obj.get_balnc(login)," Rs")
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
                balnc=obj.get_balnc(login)+amount
                obj.set_balnc(login,balnc)
                print("                     Your new balance is: ", obj.get_balnc(login))

                trans_typ="credit"
                obj.set_record_transaction(login,trans_typ,amount)
                print("                     *********************************************")
                val=input("                     For Main Menu: Press(Enter) ")
                pg_template(login)
            elif servs=="4":
                # pg_template(login)

                # print("                     Logged Out.")

                logio="logout"
                obj.set_record_login_out(login,logio)
                will=False
            elif servs=="5":
                pg_template(login)

                obj.user_history(login)
                val=input("                     For Main Menu: Press(Enter) ")
                pg_template(login)


