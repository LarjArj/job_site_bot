import PySimpleGUI as sg

# Define the window's contents
layout = [[sg.Text("What kind of job are you interested in")],sg.Text("Please Enter a Location")]
          [sg.Input(key='-INPUT-')],
          [sg.Text(size=(40,1), key='-OUTPUT-')],
          [sg.Button('Ok'), sg.Button('Quit')]]

# Create the window
window = sg.Window('Job Bot', layout)

# Display and interact with the Window using an Event Loop
while True:
    event, values = window.read()
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    # Output a message to the window
    window['-OUTPUT-'].update('Hello ' + values['-INPUT-'] + "! Thanks for trying Using")

# Finish up by removing from the screen
window.close()

#while True:
    #event, values = window.read()
    




#input-clock-output



class UI_Manager:
    def __init__(self):
        self.firstWindow = None






def initFirstWindow():
    layout = 
    [[sg.Text("What kind of job are you interested in")],
    sg.Text("Please Enter a Location")]
          [sg.Input(key='-INPUT-')],
          [sg.Text(size=(40,1), key='-OUTPUT-')],
          [sg.Button('Ok'), sg.Button('Quit')]]

    # Create the window
    window = sg.Window('Job Bot', layout)

# Display and interact with the Window using an Event Loop
    while True:
    event, values = window.read()
        # See if user wants to quit or window was closed
        if event == sg.WINDOW_CLOSED or event == 'Quit':
            break
    # Output a message to the window
     window['-OUTPUT-'].update('Hello ' + values['-INPUT-'] + "! Thanks for trying Using")

# Finish up by removing from the screen
    window.close()



def initializeSecondWindow():
    layout = [[sg.Text("What kind of job are you interested in")],sg.Text("Please Enter a Location")]
          [sg.Input(key='-INPUT-')],
          [sg.Text(size=(40,1), key='-OUTPUT-')],
          [sg.Button('Ok'), sg.Button('Quit')]]

# Create the window
    window = sg.Window('Job Bot', layout)

# Display and interact with the Window using an Event Loop
    while True:
        event, values = window.read()
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    # Output a message to the window
    window['-OUTPUT-'].update('Hello ' + values['-INPUT-'] + "! Thanks for trying Using")

# Finish up by removing from the screen
window.close()  