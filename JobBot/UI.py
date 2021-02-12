import PySimpleGUI as sg

#import NLP
# Define the window's contents
layout = [[sg.Text("What kind of job are you interested in")],
          [sg.Input(key='-INPUT-')],[sg.Text("Please Enter a Location")],[sg.Input(key='-INPUT-')],
          [sg.Text(size=(40,1), key='-OUTPUT-')],
          [sg.Button('Search')]]

# Create the window
window = sg.Window('Job Bot', layout)

# Display and interact with the Window using an Event Loop
while True:
    event, values = window.read()
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Search':
        break
    # Output a message to the window
    window['-OUTPUT-'].update("Finding...most common skills and requiremets from relavant job listings")
    #'Hello ' + values['-INPUT-'] + "! Thanks for trying Using")

# Finish up by removing from the screen
window.close()

job,location = values['-INPUT-'],values['-INPUT-0']

print(job+","+location)

#values=




#while True:
    #event, values = window.read()
    




# #input-clock-output



# class UI_Manager:

      
#     def FirstWindow(self):
#         layout = [[sg.Text("What kind of job are you interested in")],
#                  [sg.Text("Please Enter a Location")],[sg.Input(key='-INPUT-')],
#                  [sg.Text(size=(40,1), key='-OUTPUT-')],[sg.Button('Ok'), sg.Button('Quit')]]

#     # Create the window
#         window = sg.Window('Job Bot', layout)

# # Display and interact with the Window using an Event Loop
#         while True:
#             event, values = window.read()
#         # See if user wants to quit or window was closed
#             if event == sg.WINDOW_CLOSED or event == 'Quit':
#                 break
#     # Output a message to the window
#             window['-OUTPUT-'].update('Hello ' + values['-INPUT-'] + "! Thanks for trying Using")

# # Finish up by removing from the screen
#         window.close()



#     def SecondWindow(self):
#         layout = [[sg.Text("What kind of job are you interested in")],sg.Text("Please Enter a Location")]
#             [sg.Input(key='-INPUT-')],
#             [sg.Text(size=(40,1), key='-OUTPUT-')],
#             [sg.Button('Ok'), sg.Button('Quit')]]

# # Create the window
#         window = sg.Window('Job Bot', layout)

# # Display and interact with the Window using an Event Loop
#         while True:
#             event, values = window.read()
#     # See if user wants to quit or window was closed
#         if event == sg.WINDOW_CLOSED or event == 'Quit':
#             break
#     # Output a message to the window
#             window['-OUTPUT-'].update('Hello ' + values['-INPUT-'] + "! Thanks for trying Using")

# # Finish up by removing from the screen
#         window.close()  


        