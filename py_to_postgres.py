from ast import Return
from asyncio.windows_events import NULL
from tkinter import EXCEPTION
from typing import final
from unittest import skip
from clear_console import *
import psycopg2

from date_time import *

def check_login_prsnt(login):
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
      

def check_pswd_prsnt(login,passwrd):
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
    
def get_name_of_account_owner(login):
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

def get_balnc(login):
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

def set_balnc(login,balance):
    conn=psycopg2.connect("dbname=postgres user=postgres password=zeeshan,09")
    cur=conn.cursor()
    string="update users set balance={blnc} where personid='{lgin}'".format(blnc=balance,lgin=login)
    cur.execute(string)
    conn.commit()
    cur.close()
    conn.close()

def set_new_user_record(login,name,paswrd,balnc):
    conn=psycopg2.connect("dbname=postgres user=postgres password=zeeshan,09")
    cur=conn.cursor()
    string="INSERT INTO users (personid, name, password, balance) VALUES ('{lgin}','{nam}','{pswd}',{blnc});".format(lgin=login,nam=name,pswd=paswrd,blnc=balnc)
    cur.execute(string)
    conn.commit()
    cur.close()
    conn.close()

def set_record_login_out(login,logio):
    conn=psycopg2.connect("dbname=postgres user=postgres password=zeeshan,09")
    cur=conn.cursor()
    val=""
    if logio=="login":
        val="logged in"
    elif logio=="logout":
        val="logged out"
    # string="INSERT INTO user_history (personid, datetime,login_out,transaction_type,amount,remaining_balance) VALUES ('{p}','{dt}','{log}',{tt},{am},{rb});".format(p=login,dt,log=val,tt=NULL,am=NULL,rb=get_balnc(login))
    string="INSERT INTO user_history (personid,login_out,remaining_balance) VALUES ('{}', '{}', {});".format(login,val,get_balnc(login))
    cur.execute(string)
    conn.commit()
    cur.close()
    conn.close()

def set_record_transaction(login,trans_typ,amount):
    conn=psycopg2.connect("dbname=postgres user=postgres password=zeeshan,09")
    cur=conn.cursor()
    val=""
    if trans_typ=="debit":
        val="account debited"
    elif trans_typ=="credit":
        val="account credited"
    # string="INSERT INTO user_history (personid, datetime,login_out,transaction_type,amount,remaining_balance) VALUES ('{p}','{dt}','{log}',{tt},{am},{rb});".format(p=login,dt,log=val,tt=NULL,am=NULL,rb=get_balnc(login))
    string="INSERT INTO user_history (personid,transaction_type,amount,remaining_balance) VALUES ('{}','{}',{},{});".format(login,val,amount,get_balnc(login))
    cur.execute(string)
    conn.commit()
    cur.close()
    conn.close()

def user_history(login):
    conn=psycopg2.connect("dbname=postgres user=postgres password=zeeshan,09")
    cur=conn.cursor()
    # string="INSERT INTO user_history (personid, datetime,login_out,transaction_type,amount,remaining_balance) VALUES ('{p}','{dt}','{log}',{tt},{am},{rb});".format(p=login,dt,log=val,tt=NULL,am=NULL,rb=get_balnc(login))
    string="select * from user_history where personid='{}'".format(login)
    cur.execute(string)
    conn.commit()
    clearConsole()
    print("Welcome to PAK Bank".center(os.get_terminal_size().columns," "))
    print("                     ")
    for item in cur.fetchall():
        print("                     record: ",item) #21spaces before record
    cur.close()
    conn.close()





    


       
    
    
