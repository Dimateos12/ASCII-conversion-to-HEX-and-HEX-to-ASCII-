import PySimpleGUI as sg
import main as data

sg.theme('DarkBlue')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Konwerter Liczb Hex - > ASCII i ASCII -> Hex by Mateusz Jabłoński '), ],
            [sg.Text('Wpisz swoj tekst  '), sg.InputText(), ],
            [sg.Button('ASCII->HEX'), sg.Button('HEX->ASCII'), sg.Button('Exit')] ]

# Create the Window
window = sg.Window('Konwerter Liczb Hex - > ASCII i ASCII -> Hex by Mateusz Jabłoński', layout, margins=(200, 100))
text = window.read()
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    elif event == 'HEX->ASCII':
        sg.popup(data.HEX_to_ASCII(str(values[0])), title='WYNIK')

    elif event == 'ASCII->HEX':
        sg.popup(data.ASCII_to_HEX(str(values[0])), title='WYNIK')

window.close()