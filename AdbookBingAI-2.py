# You can create an address book using Python with the help of PySimpleGUI and CSV module³⁵. PySimpleGUI is a Python GUI framework that allows you to create simple and easy-to-use graphical user interfaces⁵. CSV module provides functionality to read from and write to CSV files³.

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


# This code creates a simple GUI that allows you to enter a name and phone number and save it to a CSV file named `contacts.csv`. You can also retrieve all contacts from the CSV file using the `get_contacts()` function.

# I hope this helps!

# Source: Conversation with Bing, 4/15/2023(1) GitHub - Vidito/contact_book_pysimplegui: Save Contacts to CSV and .... https://github.com/Vidito/contact_book_pysimplegui Accessed 4/15/2023.
# (2) Cookbook - PySimpleGUI. https://www.pysimplegui.org/en/latest/cookbook/ Accessed 4/15/2023.
# (3) Learn How to Create Address Book in Python - DataFlair. https://data-flair.training/blogs/address-book-in-python/ Accessed 4/15/2023.
# (4) Create Address Book in Python – Using Tkinter - GeeksForGeeks. https://www.geeksforgeeks.org/create-address-book-in-python-using-tkinter/ Accessed 4/15/2023.
# (5) Build a Contact Book GUI in Python | Save to CSV | PySimpleGUI Project .... https://www.youtube.com/watch?v=d1y-LqK9QzU Accessed 4/15/2023.