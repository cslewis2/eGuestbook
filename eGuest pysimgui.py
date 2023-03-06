import PySimpleGUI as sg

'''
    Example of GUI
'''

def main():
    sg.theme('DarkGreen4')

    column1 = [
        [sg.Text('Column 1', background_color=sg.DEFAULT_BACKGROUND_COLOR,
              justification='center', size=(10, 1))],
    ]

    layout = [
        [sg.Text('eGuest.net', size=(30, 1), font=("Helvetica", 25))],
        [sg.Text('Simplify Text')],
        [sg.InputText('USER DATA INPUT HERE??', key='in1')],
        [sg.Text('_' * 80)],
        #[sg.Text ]
        [sg.Text('Choose A Folder', size=(35, 1))],
        [sg.Text('Your Folder', size=(15, 1), justification='right'),
         sg.InputText('Default Folder', key='folder'), sg.FolderBrowse()],
        [sg.Button('Exit'),
         sg.Text(' ' * 40), sg.Button('SaveSettings'), sg.Button('LoadSettings')]
    ]

    window = sg.Window('Form Fill Demonstration', layout, default_element_size=(40, 1), grab_anywhere=False)

    while True:
        event, values = window.read()

        if event == 'SaveSettings':
            filename = sg.popup_get_file('Save Settings', save_as=True, no_window=True)
            window.SaveToDisk(filename)
            # save(values)
        elif event == 'LoadSettings':
            filename = sg.popup_get_file('Load Settings', no_window=True)
            window.LoadFromDisk(filename)
            # load(form)
        elif event in ('Exit', None):
            break

    window.close()


if __name__ == '__main__':
    main()

