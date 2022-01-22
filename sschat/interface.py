#INTERFACE
import mysql.connector as cyber
from sschat.dbinfo import *
from sschat.options import *

handler1=cyber.connect(host=host1, user=user1, password=pass1, database=db1)
cursor=handler1.cursor()
cmd='select * from users'
cursor.execute(cmd)


fetch=cursor.fetchall()
count=len(fetch)+1
count1=str(count)


def login():
    user_id=id1
    user_password=pass1
    user_name=sup[2]
    user_name_id=open('user_name_id.csv','w')
    objz=csv.writer(user_name_id)
    objz.writerow([user_name,user_id])
    user_name_id.close()
    show_options()

def check(id1,pass1):
    k=1
    global sup
    for tup in fetch:
        if tup[0]==id1:
            global sup
            sup=tup
            k=0
            break
        else:
            continue

    if k==1:
        print("YOU DONT HAVE AN EXISTING ACCOUNT. PLEASE RESTART PROGRAM AND CREATE ONE")
    else:
        if sup[1]==pass1:
            login()
        else:
            print("INCORRECT PASSWORD")

    
def create(name,password):
    global id1
    if count<10:
        id1='000'+count1
    elif count<100 and count>9:
        id1='00'+count1
    else:
        id1='0'+count1
    cmd="insert into users(id,password,name) values(%s,%s,%s)"
    val=(id1,password,name)
    cursor.execute(cmd,val)
    handler1.commit()
    cmd4='create table id'+id1+'(receiver_id char(4),message varchar(1024))'
    cursor.execute(cmd4)
    handler1.commit
    print("YOUR UNIQUE ID IS",id1,", REMEMBER IT FOR FURTHER USE")
    print("RESTART PROGRAM TO LOGIN")
    a=2
    while a>1:
        a+=1
        

if __name__=="__main__":
    print("WELCOME TO SS CHATS")
    print()
    s=int(input('''
    1.LOG IN
    2.CREATE ACCOUNT
    '''))

    if s==1:
        id1=str(input("ENTER YOUR UNIQUE ID:"))
        pass1=input("ENTER YOUR PASSWORD:")
        check(id1,pass1)

    elif s==2:
        name=input("ENTER YOUR NAME:")
        password=input("CREATE PASSWORD:")
        create(name,password)





    handler1.commit()
