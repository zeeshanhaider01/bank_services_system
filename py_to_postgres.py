import psycopg2

from date_time import *

def usr_record():
    usrs_record=[]
    conn=psycopg2.connect("dbname=postgres user=postgres password=zeeshan,09")
#     host="localhost",
#     dbname="bank_services_system",
#     user="postgres",
#     password="zeeshan,09",
#     port="5432"
# ) 
    print("timestamp: ",psycopg2.Timestamp(datetime.now()))
    cur=conn.cursor()
    # insert_script="insert into Users (PersonID,Name,Password,Balance) values (%s,%s,%s,%s)"
    # insert_val=["asad","asadullah",1234,70000]
    # cur.execute(insert_script,insert_val)
    # conn.commit()

    # cur.execute('select * from users')
    # for record in cur.fetchall():
    #     print(record)
    cur.execute('select * from users')
    for record in cur.fetchall():
        arr=list(record)
        usrs_record.append(arr)
    print(usrs_record)
    conn.close()
    return usrs_record

arr=usr_record()
print(arr)
for record in arr:

    if "asad" in record:
        print("login id is present.")
    else:
        print("if else not working")
