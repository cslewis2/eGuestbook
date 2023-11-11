
# from datetime import date
import os.path
import csv
import PySimpleGUI as sg


def save_contact(Visit_Date,Guest_Fname,Guest_Lname,Guest_Address,Guest_City,Guest_State,Member_Name):
    with open('eGuestData--8877.csv', mode='a', newline='') as file:
        fieldnames = ['Visit_Date','Guest_Fname','Guest_Lname','Guest_Address','Guest_City','Guest_State','Member_Name']
        writer = csv.writer(file)
        writer.writerow({Visit_Date,Guest_Fname,Guest_Lname,Guest_Address,Guest_City,Guest_State,Member_Name})
      
def get_contacts():
    contacts = []
    with open('contacts.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            contacts.append(row)
    return contacts

               
def main():
    
    sg.theme('DarkAmber')
    layout =[[sg.Text('Please enter guest information')],
    [sg.Text('Visit_Date mm/dd/yyyy', size =(15, 1)), sg.InputText()],       
    [sg.Text('Guest first name', size =(15, 1)), sg.InputText()],
    [sg.Text('Guest last name', size =(15, 1)), sg.InputText()],
    [sg.Text('Guest address', size =(20, 1)), sg.InputText()],
    [sg.Text('Guest city', size =(20, 1)), sg.InputText()],
    [sg.Text('Guest state', size =(20, 1)), sg.InputText()],
    [sg.Text('Guest zip', size =(20, 1)), sg.InputText()],
    [sg.Text('Member name', size =(15, 1)), sg.InputText()],
    [sg.Text('Staff initials', size =(15, 1)), sg.InputText()],
    [sg.Save(), sg.Exit()]]
    
    window = sg.Window('eGuest with PySimple GUI', layout)
    # event, values = window.read()
    # window.close()

    while True:
        event, values = window.read()
        if event == 'Save':
            save_contact=(values['Visit_Date'],values['Guest_Fname'],values['Guest_Lname'],values['Guest_Address'],values['Guest_City'],values['Guest_State'],values,['Member_Name'])
            sg.Popup('Contact saved!')
        elif event == 'Exit':
            break
    window.close()

if __name__ == '__main__':
    main()
