import mysql.connector as mycon
import csv
from sschat.dbinfo import *
handler=mycon.connect(host=host1,user=user1,password=pass1,database=db1)
cursor=handler.cursor()

user_name_id=open('user_name_id.csv','r')
cont_name_id=open('cont_name_id.csv','r')
obj1=csv.reader(user_name_id)
obj2=csv.reader(cont_name_id)
for i in obj1:
    if len(i)==0:
        pass
    else:
        user_id=i[1]
        break
for i in obj2:
    if len(i)==0:
        pass
    else:
        cont_id=i[1]
        break
user_name_id.close()
cont_name_id.close()



def receive_chat(cont_id):
    cmd='select message from id'+cont_id+' where receiver_id='+user_id
    cursor.execute(cmd)
    fetch1=cursor.fetchall()
    cmd2='delete from id'+cont_id+' where receiver_id='+user_id
    cursor.execute(cmd2)
    handler.commit()

    file_name='id'+cont_id+'.csv'
    f=open(file_name,'a')
    obj2=csv.writer(f)
    if len(fetch1)==0:
        pass
    else:
        for i in fetch1:
            obj2.writerow(['oth',i[0]])


print("PLEASE MINIMIZE THIS WINDOW")
b=1
while b==1:
    handler=mycon.connect(host=host1,user=user1,password=pass1,database=db1)
    cursor=handler.cursor()
    receive_chat(cont_id)
    b=1
