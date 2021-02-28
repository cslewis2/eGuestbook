#test test testt!!! THIS SHOULD BE UPLOADED TO GITHUB
#C:\Users\clarence\source\repos\eGuestbook\EGUEST REDO2.py
##WORK FROM THIS CODE AS OF 7/29/2019
from random import randint
from datetime import date
import csv
import os.path

"""Simple guest card generates todays date, guest ID, guest name,guest address and member name then stores everything in eGuestREDO.csv"""

print ('HVTC GUEST eCARD')
print ('Todays date is ',(date.today()))

total_guests=(int(input('how many guests today?  ')))
for i in range (0,total_guests):
    def visit_date():
        """generates datestamp comprising todays date"""
        guest_date=(date.today())
        return guest_date

    #def guest_name():
    #    guest_first=(str.capitalize(input('guest first name?  ')))
    #    guest_last=(str.capitalize(input('guest last name?  ')))
    #    guest_name_merge=' '.join([guest_first,guest_last])
    #    return guest_name_merge #name_merge

    def guest_fname():
        guest_first=(str.capitalize(input('guest first name?  ')))           
        return guest_first

    def guest_lname():
        guest_last=(str.capitalize(input('guest last name?  ')))        
        return guest_last

    def guest_address():
        """generates guest address"""
        address=(input('what is guests street address?  '))
        return address
    
    def guest_city():
        '''generates guest city'''
        city=(string.capitalize(input('what city is guest from?  ')))
        return city

    def guest_state():
        '''generates guest state'''
        state=str.upper(input('what state is guest from?  '))
        return state

    def member_name():
        """generates merged member first and last names"""
        member_first=(str.capitalize(input('member first name?  ')))
        member_last=(str.capitalize(input('member last name?  ')))
        member_name_merge=(' '.join([member_first,member_last]))
        return member_name_merge

file_exists=os.path.isfile('eGuestREDO2.csv')

with open('eGuestREDO2.csv', 'a', newline='') as csvfile:
        fieldnames = ['Visit_Date','Guest_Fname','Guest_Lname','Guest_Address','Guest_City','Guest_State','Member_Name']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()

        for a in range (0,total_guests):
                writer.writerow({'Visit_Date':visit_date(),'Guest_Fname':guest_fname(),\
                'Guest_Lname':guest_lname(),'Guest_Address':guest_address(),\
                'Guest_City':guest_city(),'Guest_State':guest_state(),'Member_Name':member_name()\
                })
#there is 1 and only 1 set of function calls at the end of scrit when writing 
#csv to disk...otherwise will call a second #time at the end and overwrite
#original data input by user