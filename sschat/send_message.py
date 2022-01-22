import mysql.connector as mycon
import os
import csv
from sschat.dbinfo import *
handler1=mycon.connect(host=host1,user=user1,password=pass1,database=db1)
cursor=handler1.cursor()


def send_message():
    mess=input("ENTER MESSAGE:")
    if mess=='/quit':
        a=0
    else:
        cmd='insert into id'+user_id+' values'+'('+cont_id+','+'"'+mess+'"'+')'
        cursor.execute(cmd)
        handler1.commit()
        file_name='id'+cont_id+'.csv'
        f=open(file_name,'a')
        obj=csv.writer(f)
        obj.writerow(['you',mess])
        f.close()
        a=1


def start_chatting():
    cmd1='start /min receiving.py'
    cmd2='start SHOW_CHAT.py'
    os.system(cmd1)
    os.system(cmd2)
    user_name_id=open('user_name_id.csv','r')
    cont_name_id=open('cont_name_id.csv','r')
    obj1=csv.reader(user_name_id)
    obj2=csv.reader(cont_name_id)
    global user_id
    global cont_id
    for i in obj1:
        if len(i)==0:
            continue
        else:
            user_id=i[1]
    for i in obj2:
        if len(i)==0:
            continue
        else:
            cont_id=i[1]
    user_name_id.close()
    cont_name_id.close()
    a=1
    while a==1:
        handler1=mycon.connect(host=host1,user=user1,password=pass1,database=db1)
        cursor=handler1.cursor()
        send_message()
    return


    
