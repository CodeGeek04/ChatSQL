import csv


user_name_id=open('user_name_id.csv','r')
cont_name_id=open('cont_name_id.csv','r')
obj1=csv.reader(user_name_id)
obj2=csv.reader(cont_name_id)
for i in obj1:
    if len(i)==0:
        pass
    else:
        user_name=i[0]
        user_id=i[1]
        break
for i in obj2:
    if len(i)==0:
        pass
    else:
        cont_name=i[0]
        cont_id=i[1]
        break
user_name_id.close()
cont_name_id.close()


file_name='id'+cont_id+'.csv'
messes=open(file_name,'r')
obj1=csv.reader(messes)
l1=0
l2=0
for i in obj1:
    if len(i)==0:
        pass
    else:
        l1+=1
        if i[0]=='oth':
            print(cont_name,':',i[1])
        else:
            print('You:',i[1])
                
            

def print_latest():
    message_list=list(obj1)
    mssg2=message_list[-2][1]
    sen=message_list[-2][0]
    if sen=='oth':
        print(cont_name,':',mssg2)
    else:
        print('You:',mssg2)



    
e=1    
while e==1:
    filef=open(file_name,'r')
    objf=csv.reader(filef)
    l2=0
    for i in objf:
        if len(i)==0:
            pass
        else:
            l2+=1
    filef.close()
    if l2==l1:
        pass
    else:
        print_latest()
    l1=l2
    e=1
filef.close()
