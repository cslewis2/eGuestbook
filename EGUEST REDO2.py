

##WORK FROM THIS CODE AS OF 7/28/2019
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

    def guest_name():
        guest_first=(str.capitalize(input('guest first name?  ')))
        guest_last=(str.capitalize(input('guest last name?  ')))
        guest_name_merge=' '.join([guest_first,guest_last])
        return guest_name_merge #name_merge

        def guest_fname():
            pass
        def guest_lname():
            pass

    def guest_address():
        """generates guest address"""
        address=(input('what is guests street address?  '))
        #city_state=(input('what is guest city and state?  '))
        return address

    def member_name():
        """generates merged member first and last names"""
        member_first=(str.capitalize(input('member first name?  ')))
        member_last=(str.capitalize(input('member last name?  ')))
        member_name_merge=(' '.join([member_first,member_last]))
        return member_name_merge

file_exists=os.path.isfile('eGuestREDO2.csv')#
with open('eGuestREDO.csv', 'a', newline='') as csvfile:
#function open ('filename.CSV),r-read,w-write-a-append (add to) as filetype csvfile:
#use with because it implicitly calls a file close for the file when done
        fieldnames = ['Visit_Date','Guest_Name','Guest_Address','Member_Name']
#fieldnames function defines ROW 1 in spreadsheet, column headers in single quotes in form of a list
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#dictwriter is a dictionary utility function for python created csv files...transcribes a python dictionary to csv file
        if not file_exists:#
            writer.writeheader()#

        for a in range (0,total_guests):
                writer.writerow({'Visit_Date':visit_date(),'Guest_Name':guest_name(),\
                'Guest_Address':guest_address(),'Member_Name':member_name()\
                })
#there is 1 and only 1 set of function calls at the end when writing csv to disk...otherwise will call a second #time at the end and overwrite original data input by user