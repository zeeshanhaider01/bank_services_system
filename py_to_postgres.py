from clear_console import *
import psycopg2
from tabulate import tabulate

class database_gateway:
    # def __init__(self):
    #     pass
    def check_login_prsnt(self,login):
            
            conn=psycopg2.connect("dbname=postgres user=postgres password=zeeshan,09")
            cur=conn.cursor()
            string="SELECT personid FROM users where personid='{lgin}';".format(lgin=login)
            # print("string: ",string)
            cur.execute(string)
            val=cur.fetchall()
            # print("val: ",val)
            if val==[]:
                cur.close()
                conn.close()
                return False

            elif val!=None:
                cur.close()
                conn.close()# print("cur.fetchall(): ",cur.fetchall())
                return True
        

    def check_pswd_prsnt(self,login,passwrd):
      
        conn=psycopg2.connect("dbname=postgres user=postgres password=zeeshan,09")
        cur=conn.cursor()
        string="SELECT personid FROM users where personid='{lgin}' AND password='{pswd}';".format(lgin=login, pswd=passwrd)
        cur.execute(string)
        val=cur.fetchall()
        # print("val: ",val)
        if val==[]:
            cur.close()
            conn.close()
            return False
        else:
            cur.close()
            conn.close()
            return True
        
    def get_name_of_account_owner(self,login):
        
        conn=psycopg2.connect("dbname=postgres user=postgres password=zeeshan,09")
        cur=conn.cursor()
        string="select name from users where personid='{}'".format(login)
        cur.execute(string)
        val=cur.fetchall()
        for item in val:
            for elm in item:
                cur.close()
                conn.close()
                return elm

    def get_balnc(self,login):
       
        conn=psycopg2.connect("dbname=postgres user=postgres password=zeeshan,09")
        cur=conn.cursor()
        string="select balance from users where personid='{lgin}'".format(lgin=login)
        cur.execute(string)
        val=cur.fetchall()
        for item in val:
            for elm in item:
                cur.close()
                conn.close()
                return elm

    def set_balnc(self,login,balance):
        
        conn=psycopg2.connect("dbname=postgres user=postgres password=zeeshan,09")
        cur=conn.cursor()
        string="update users set balance={blnc} where personid='{lgin}'".format(blnc=balance,lgin=login)
        cur.execute(string)
        conn.commit()
        cur.close()
        conn.close()

    def set_new_user_record(self,login,name,paswrd,balnc):
       
        conn=psycopg2.connect("dbname=postgres user=postgres password=zeeshan,09")
        cur=conn.cursor()
        string="INSERT INTO users (personid, name, password, balance) VALUES ('{lgin}','{nam}','{pswd}',{blnc});".format(lgin=login,nam=name,pswd=paswrd,blnc=balnc)
        cur.execute(string)
        conn.commit()
        cur.close()
        conn.close()

    def set_record_login_out(self,login,logio):
       
        conn=psycopg2.connect("dbname=postgres user=postgres password=zeeshan,09")
        cur=conn.cursor()
        val=""
        if logio=="login":
            val="logged in"
        elif logio=="logout":
            val="logged out"
        # string="INSERT INTO user_history (personid, datetime,login_out,transaction_type,amount,remaining_balance) VALUES ('{p}','{dt}','{log}',{tt},{am},{rb});".format(p=login,dt,log=val,tt=NULL,am=NULL,rb=get_balnc(login))
        string="INSERT INTO user_history (personid,login_out,remaining_balance) VALUES ('{}', '{}', {});".format(login,val,database_gateway.get_balnc(self,login))
        cur.execute(string)
        conn.commit()
        cur.close()
        conn.close()

    def set_record_transaction(self,login,trans_typ,amount):
        conn=psycopg2.connect("dbname=postgres user=postgres password=zeeshan,09")
        cur=conn.cursor()
        val=""
        if trans_typ=="debit":
            val="account debited"
        elif trans_typ=="credit":
            val="account credited"
        string="INSERT INTO user_history (personid,transaction_type,amount,remaining_balance) VALUES ('{}','{}',{},{});".format(login,val,amount,database_gateway.get_balnc(self,login))
        cur.execute(string)
        conn.commit()
        cur.close()
        conn.close()

    def user_history(self,login):
        
        conn=psycopg2.connect("dbname=postgres user=postgres password=zeeshan,09")
        cur=conn.cursor()
        string="select * from user_history where personid='{}'".format(login)
        cur.execute(string)
        conn.commit()
        record=[]
        heads=["                     ","User ID","Date(Y/M/D) Time(H/M/S)","Login/out","Transaction Type","Amount","Remaining Balance","                     "]
        for item in cur.fetchall():
            arr=["                     "]
            arr.extend(item)
            spc=["                     "]
            arr.extend(spc)
            record.append(arr)
        # for item in cur.fetchall():
        #     record.append(item)
        print(tabulate(record,headers=heads))
            # print("                     record: ",item) #21spaces before record

        cur.close()
        conn.close()





    


       
    
    
