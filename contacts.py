#CONTACTS
import csv
#from sschat.options import *
#import os
#print(os.getcwd())


def add_contact(name,id3):
    global file_name
    f=open('contacts.csv','a')
    obj=csv.writer(f)
    obj.writerow([name,id3])
    file_name='id'+id3+'.csv'
    file2=open(file_name,'w')
    file2.close()
    f.close()
    

#IMPORT NAME AND ID FROM INTERFACE
#def show_contacts():


def show_contacts():
    f=open('contacts.csv','r')
    obj=csv.reader(f)
    for i in obj:
        if len(i)==0:
            pass
        else:
            print(i[0],"    ",i[1],end="\n")
    f.close()


def search_contact(n):
    file1=open('contacts.csv','r')
    obj1=csv.reader(file1)
    for i in obj1:
        if len(i)==0:
            pass
        else:
            if i[1]==n:
                name=i[0]
                break
            else:
                continue
    return name
