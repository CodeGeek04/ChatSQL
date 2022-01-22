#options
import csv
from sschat.contacts import *
from sschat.send_message import *



def show_options_k(a):
    
    global id2
    if a==1:
        show_contacts()
        show_options()

    elif a==2:
        id2=str(input("ENTER CONTACT ID:"))
        name=search_contact(id2)
        file1=open('cont_name_id.csv','w')
        obj1=csv.writer(file1)
        obj1.writerow([name,id2])
        file1.close()
        print("PLEASE OPEN CHATTING AND RECIEVING PROGRAMS")
        start_chatting()
    
    else:
        name=input("ENTER CONTACT NAME:")
        id3=str(input("ENTER CONTACT ID:"))
        add_contact(name,id3)
        print('CONTACT ADDED SUCCESSFULLY')
        show_options()



def show_options():
    a=int(input('''
SELECT ANY ONE OF THE FOLLOWING:
1.SHOW CONTACTS
2.SELECT A CONTACT
3.ADD CONTACT
-->'''))
    show_options_k(a)
    
    
