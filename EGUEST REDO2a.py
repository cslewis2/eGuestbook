
#stillfunctional, 
#wild wild world of gui bolt on...
import PySimpleGUI as sg
from random import randint
from datetime import date
import csv
import os.path

"""Simple guest card generates todays date, guest ID, guest name,guest address and member name then stores everything in eGuestREDO.csv"""
layout = [
        [sg.Text('All graphic widgets in one form!', size=(30, 1), font=("Helvetica", 25))],
        [sg.Text('Here is some text.... and a place to enter text')],
        [sg.InputText('This is my text', key='in1')]]
# sg.Window(title='HVTC eGuest Book',layout=[[sg.Button('OK')]],margins=(110,50)).read()
sg.Window[(title='hvtc eGuest Book')],layout=[sg.Text[('Here is some text.... and a place to enter text')],
sg.InputText[('This is my text', key='in1')]
#event loop

while True:
    event,values=window.read()
    #end program if user closes window or presses OK button
    if event=='OK' or event==sg.WIN_CLOSED:
        break
window.close()



print ('HVTC GUEST eCARD')
print ('Todays date is ',(date.today()))

total_guests=(int(input('how many guests today?  ')))
for i in range (0,total_guests):
    def visit_date():
        """generates datestamp comprising todays date"""
        guest_date=(date.today())
        return guest_date

    def guest_fname():
        guest_first=(str.capitalize(input('guest first name?  ')))           
        return guest_first

    def guest_lname():
        guest_last=(str.capitalize(input('guest last name?  ')))        
        return guest_last

    def guest_address():
        """generates guest address"""
        address=(str.capitalize(input('what is guests street address?  ')))
        return address
    
    def guest_city():
        '''generates guest city'''
        city=(str.capitalize(input('what city is guest from?  ')))
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

file_exists=os.path.isfile('eGuestREDO1225222.csv')

with open('eGuestREDO1225222.csv', 'a', newline='') as csvfile:
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