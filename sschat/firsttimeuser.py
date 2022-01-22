#FIRST-TIME USER
import csv


file1=open('contacts.csv','w')
obj=csv.writer(file1)
obj.writerow(["NAME",'ID'])
file1.close()
