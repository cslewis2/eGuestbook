# Dev environment(s) python 3.3/android 8.1/qpython3 \\ python 3.52/windows 10/ms visual studio 2013
import random
from datetime import date
"""Key generator produces a 4 digit non-random number appended to last 4 letters of a last name. using for gGuest IDs"""

#print (date.today)
#put this whole thing inside a for loop and it should be ok. next move--store as csv
def guestid():
    """generates a list of lists with 4 digit id + 4xlast name as list of lists"""    
    finalkeys=[]
    keynum=(int(input('how many keys do you need?  ')))
    for i in range (0,keynum):
        first=(str(input('guest first name?  ')))
        last=(str(input('guest last name?  ')))
        keyid=(((str(random.randint(1000,9999))+last[0:4])))
        finalkeys.append(keyid)
    return finalkeys
#print (guestid())--NO!!

def guestname():
    """generates merged member first and last names"""
    guestlast=(str(input('guest last name?  ')))
    guestfirst=(str(input('guest first name?  ')))
    gstname=[guestlast,guestfirst]
    gstnamemrg=(' '.join(gstname))
    return gstnamemrg
def guestaddress():
    """generates merged guest id and address"""
    address=(str(input('what is guests address?  ')))
    return address

def membername():
    """generates merged member first and last names"""
    memfirst=(str(input('member first name?  ')))
    memlast=(str(input('member last name?  ')))
    memname=[memfirst,memlast]
    memnamemrg=(' '.join(memname))
    return memnamemrg
#print (membername())--NO!! this is a second call to the function!!!!!

#merge=[guestid()[0],guestaddress()]
#print(' '.join(merge))
eGuest=[guestid(),guestname(),guestaddress(),membername()]
print (eGuest)
#remember, print statements are also calling the function. if active above, 
#would ask for id and address twice... as done above, merge has first & only call on both functions
#keep going....
