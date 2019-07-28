##DO NOT USE THIS CODE!!!
##THIS FILE IS NOT FINAL APP. GENERATES MEMBER IDs AND HAS LOGICAL ERROR WITH FN CALLS...

from random import randint
from datetime import date
import csv

"""Simple guest card generates todays date, guest ID, guest name,guest address and member name then stores everything in eGuestFinal.csv"""

print ('HVTC GUEST eCARD')
print ('Todays date is ',(date.today()))

total_guests=(int(input('how many guests today?  ')))
for i in range (0,total_guests):
    def visit_date():
        """generates datestamp comprising todays date"""        
        guest_date=(date.today())
        return guest_date

    #def guest_ID():
    #    """generates a nonrandom 5 digit number to use as guestID"""
    #    rnd_ID=((str(randint(10000,99999))))
    #    return rnd_ID

    def guest_ID():
        """generates a list of lists with 4 digit id + 4xlast name as list of lists"""    
        finalkeys=[]
        #keynum=(int(input('how many keys do you need?  ')))
        #for i in range (0,keynum):
        first=(str.capitalize(input('guest first name?  ')))
        last=(str.capitalize(input('guest last name?  ')))
        keyid=(((str(randint(1000,9999))+last[0:4])))
        finalkeys.append(keyid)
        full_name=(first,last)
        return finalkeys,full_name
    def guest_name():
        fullname=(guest_ID()[1])
        #name_merge=(' '.join (fullname[0],fullname[1]))
        return fullname #name_merge
#this is the first call for this function
#CSV file creation is second call this is why when only one id needed asks for first and last name twice. 
#have to get rid of the above call and get this down to 1 call only. 
#may need to separate name creation from ID or just go with a single id number??
#there has to be a simple fix i'm not seeing right now...

    #def guest_name():
    #    """generates merged member first and last names"""
    #    guest_first=(str.capitalize(input('guest first name?  ')))
    #    guest_last=(str.capitalize(input('guest last name?  ')))
    #    guest_name_merge=(' '.join([guest_first,guest_last]))
    #    return guest_name_merge

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

with open('eGuestFinal.csv', 'a', newline='') as csvfile:
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
