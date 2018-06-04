from random import randint
from datetime import date
import csv

"""Simple guest card generates todays date, guest ID, guest name,guest address and member name then stores everything in eGuestNEW.csv"""

print ('HVTC GUEST eCARD')
print ('Todays date is ',(date.today()))

total_guests=(int(input('how many guests today?  ')))
for i in range (0,total_guests):
    def visit_date():
        """generates datestamp comprising todays date"""        
        guest_date=(date.today())
        return guest_date

    def guest_ID():
        """generates a nonrandom 5 digit number to use as guestID"""
        rnd_ID=((str(randint(10000,99999))))
        return rnd_ID

    def guest_name():
        """generates merged member first and last names"""
        guest_first=(str.capitalize(input('guest first name?  ')))
        guest_last=(str.capitalize(input('guest last name?  ')))
        guest_name_merge=(' '.join([guest_first,guest_last]))
        return guest_name_merge

    def guest_address():
        """generates guest address"""
        address=((input('what is guests address?  ')))
        return address

    def member_name():
        """generates merged member first and last names"""
        member_first=(str.capitalize(input('member first name?  ')))
        member_last=(str.capitalize(input('member last name?  ')))
        member_name_merge=(' '.join([member_first,member_last]))
        return member_name_merge

with open('eGuestNEW.csv', 'a', newline='') as csvfile:
#function open ('filename.CSV),r-read,w-write-a-append (add to) as filetype csvfile:
#use with because it implicitly calls a file close for the file when done
        fieldnames = ['Visit_Date','Guest_ID','Guest_Name','Guest_Address','Member_Name']
#fieldnames function defines ROW 1 in spreadsheet, column headers in single quotes in form of a list
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#dictwriter is a dictionary utility function for python created csv files...transcribes a python dictionary to csv file
        writer.writeheader()
#if this line not included, will take first line of data as ROW 1...is optional with dictwriter but required otherwise
        for a in range (0,total_guests):
                writer.writerow({'Visit_Date':visit_date(),'Guest_ID':guest_ID(),'Guest_Name':guest_name(),\
                'Guest_Address':guest_address(),'Member_Name':member_name()\
                })
#there is 1 and only 1 set of function calls at the end when writing csv to disk...otherwise will call a second time
#at the end and overwrite original data input by user
