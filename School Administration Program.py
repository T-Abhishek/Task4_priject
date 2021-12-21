import csv
import os

def write_into_csv(info_list):
    if os.path.exists('student_info.csv')==True:
        with open('student_info.csv','a',newline='') as sfile:
            parser=csv.writer(sfile)
            parser.writerow(s_info_list)
    else:
        with open('student_info.csv','a',newline='') as sfile:
            parser=csv.writer(sfile)
            parser.writerow(['NAME','AGE','CONTACT NO','EMAIL ID'])
            parser.writerow(s_info_list)

condition=True
while condition:
    student_input=input("Enter Student information in the following format(Name Age Contact_Number E-mail_ID):")
    s_info_list=student_input.split(' ')
    write_into_csv(s_info_list)

    while True:
        condition_check=input("Enter (yes/no) if you want to enter information for another student:")
        if condition_check=='yes':
            condition=True
            break
        elif condition_check=='no':
            condition=False
            break
        else:
            print('enter only yes/no!')
            continue
