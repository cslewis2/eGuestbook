import datetime
import json
from random import randint
import os.path

#this works....
#def fullname ():
#    fname=input(('whats your first name? '))
#    lname=input(('whats your last name? '))
#    numb=str(randint(1000,9999))
#    jtemp=[numb,lname[:4]]
#    idp=''.join(jtemp)
#    return idp,fname,lname
#    #return (idnum,fname,lname)
#print (fullname())

#alternative way--key fn inside name fn...half step from a decorator???
visit_date=datetime.date.today()
namenum=int(input(('how many names?  ')))
if namenum <= 0:
    print ('number must be greater than zero...')

def fullname ():
    fname=input(('what guest first name? '))
    lname=input(('what is guest last name? '))
    def idnum ():
        numb=str(randint(1000,9999))
        jtemp=(numb,lname[:4].upper())
        idp=''.join(jtemp)
        return idp
        
    #def visit_date():
        #v_date=(date.today())
        #return v_date
    def guest_address():
        gst_addr=input('what is guest address?  ')
        return gst_addr
    def member_name():
        mem_name=input('what is members first and last name [format==first last]?  ')
        return mem_name
    return {idnum():(lname,fname,guest_address(),member_name())}#same as iguestredo2=single set of calls at end to capture user input data


file_exists=os.path.isfile('eGuestREDO2.csv')

datalist={}
for num in range(0,namenum):
    
    datalist.update(fullname())
#print (datalist)
    with open('guest_list.json', 'a') as fw: #can be appended to just fine...'w'will overwrite whatever's there.
        json.dump(datalist,fw)
    # write json data into filejson.dump(person_data, file_write)

#print(datetime.date.today())
# TO ADD TO DICTIONARY example--dict_name.update({'item': 3})
# save as json--above works...now to load it and count nbr of visits
#and search...tuples are changed to lists no idea how to fix it...