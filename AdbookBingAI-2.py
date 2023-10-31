
# Here's an example of how you can create an address book using PySimpleGUI and CSV module:

# python
import csv
import PySimpleGUI as sg

def save_contact(name, phone):
    with open('contacts.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, phone])

def get_contacts():
    contacts = []
    with open('contacts.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            contacts.append(row)
    return contacts

def main():
    sg.theme('DarkAmber')
    layout = [[sg.Text('Name'), sg.InputText(key='name')],
              [sg.Text('Phone'), sg.InputText(key='phone')],
              [sg.Button('Save'), sg.Button('Exit')]]
    window = sg.Window('Address Book', layout)
    while True:
        event, values = window.read()
        if event == 'Save':
            save_contact(values['name'], values['phone'])
            sg.Popup('Contact saved!')
        elif event == 'Exit':
            break
    window.close()

if __name__ == '__main__':
    main()
