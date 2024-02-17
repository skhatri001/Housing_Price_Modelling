import PySimpleGUI as sg

"""
    For Reddit - Input a value, then enter another 3 more into same input box. Store in a list
"""

layout = [  [sg.Text('Mortgage Calculator', font='Any 16')],
            [sg.Text('Home Value', justification='r', size=(16,), key='-TEXT-'), sg.Input(size=(8,1),justification='r',do_not_clear=False, key='-IN-'),sg.Text('$', justification='l', size=(12,1), key='-TEXT-')],
            [sg.Text('Down Payment', justification='r', size=(16,), key='-TEXT-'), sg.Input(size=(8,1),justification='r',do_not_clear=False, key='-IN-'),sg.Text('%', justification='l', size=(12,1), key='-TEXT-')],
            [sg.Text('Annual Interest Rate',justification='r', size=(16,), key='-TEXT-'), sg.Input(size=(8,1),justification='r',do_not_clear=False, key='-IN-'),sg.Text('%', justification='l', size=(12,1), key='-TEXT-')],
            [sg.Text('Loan Term', justification='r', size=(16,), key='-TEXT-'), sg.Input(size=(8,1),justification='r',do_not_clear=False, key='-IN-'),sg.Text('years', justification='l', size=(12,1), key='-TEXT-')],
            [sg.Button('Enter', bind_return_key=True), sg.Button('Exit')]  ]

window = sg.Window('Mortgage Calculator', layout,element_justification='center')

counter = 0
stuff_entered = []
while True:             # Event Loop
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Enter':
        stuff_entered.append(values['-IN-'])
        if counter > 2:
            break
        window['-TEXT-'].update(f'Input Value {counter+1}')
        counter += 1

window.close()
sg.popup(f'You entered {stuff_entered}')
