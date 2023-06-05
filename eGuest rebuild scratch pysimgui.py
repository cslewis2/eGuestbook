
from datetime import date
import csv
#EXAMPLE #1

import PySimpleGUI as sg
  
# Add some color
# to the window
sg.theme('DarkGrey6')     
  
# Very basic window.
# Return values using
# automatic-numbered keys
layout = [
    [sg.Text('Please enter guest Name, Address, ')],
    [sg.Text('Guest first name', size =(15, 1)), sg.InputText()],
    [sg.Text('Guest last name', size =(15, 1)), sg.InputText()],
    [sg.Text('Guest address', size =(20, 1)), sg.InputText()],
    [sg.Text('Guest city', size =(20, 1)), sg.InputText()],
    [sg.Text('Guest state', size =(20, 1)), sg.InputText()],
    [sg.Text('Guest zip', size =(20, 1)), sg.InputText()],
    [sg.Text('Member name', size =(15, 1)), sg.InputText()],
    [sg.Text('Staff initials', size =(15, 1)), sg.InputText()],


    [sg.Submit(), sg.Cancel()]
]
  #so...[sg.Text('Guest first name',size=(15,1), sg.InputText(guest_lname())]--call function here??)
window = sg.Window('eGuest with PySimple GUI', layout)
event, values = window.read()
window.close()
  
# The input data looks like a simple list 
# when automatic numbered
#output is printed to terminal as usual, how to get to csv...!
print(event, values[0], values[1], values[2])

with open('eGuestREDOpysimp.csv', 'a', newline='') as csvfile:
        fieldnames = ['Visit_Date','Guest_Fname','Guest_Lname','Guest_Address','Guest_City','Guest_State','Member_Name']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()

        for a in range (0,total_guests):
                writer.writerow({'Visit_Date':visit_date(),'Guest_Fname':guest_fname(),\
                'Guest_Lname':guest_lname(),'Guest_Address':guest_address(),\
                'Guest_City':guest_city(),'Guest_State':guest_state(),'Member_Name':member_name()\
                })



# #EXAMPLE #2
# #import PySimpleGUI as sg
# def compute_bonus(sales):
#     return sales * .25


# def main():
#     layout = [  [sg.Text('Sales Commission Calculator')],
#                 [sg.Text('How much did you sell?  $'), sg.Input(size=(8,1), key='-IN-')],
#                 [sg.Text('Your total income: '), sg.Text(size=(15,1), key='-OUT-')],
#                 [sg.Button('Calculate', bind_return_key=True), sg.Button('Exit')]  ]

#     window = sg.Window('Sales Commission Calculator', layout)

#     while True:             # Event Loop
#         event, values = window.read()
#         if event == sg.WIN_CLOSED or event == 'Exit':
#             break
#         if event == 'Calculate':
#             try:
#                 total = float(values['-IN-'])
#                 total += compute_bonus(total)
#                 window['-OUT-'].update(f'${total:.2f}')
#             except:
#                 window['-OUT-'].update('Invalid input')

#     window.close()

# if __name__ == '__main__':
#     main()