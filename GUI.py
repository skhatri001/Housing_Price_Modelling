import PySimpleGUI as sg

"""
    For Reddit - Input a value, then enter another 3 more into same input box. Store in a list
"""
layout_text = ['Home Value', 'Down Payment', 'Annual Interest Rate', 'Loan Term','Property Tax' ,'Monthly Payment', 'Annual Payment Raise']
font = ("Arial", 16)
layout = [  [sg.Text('Mortgage Calculator', font='Any 24')],
            [sg.Text(layout_text[0], justification='r', size=(19,), font=font, key='-TEXT-'), sg.Input(size=(8,1),justification='r',font=font,do_not_clear=False, key=layout_text[0]),sg.Text('$', justification='l', size=(12,1), font=font,key='-TEXT-')],
            [sg.Text(layout_text[1], justification='r', size=(19,), font=font,key='-TEXT-'), sg.Input(size=(8,1),justification='r',font=font,do_not_clear=False, key=layout_text[1]),sg.Text('%', justification='l', size=(12,1), font=font,key='-TEXT-')],
            [sg.Text(layout_text[2],justification='r', size=(19,), font=font,key='-TEXT-'), sg.Input(size=(8,1),justification='r',font=font,do_not_clear=False, key=layout_text[2]),sg.Text('%', justification='l', size=(12,1), font=font,key='-TEXT-')],
            [sg.Text(layout_text[3], justification='r', size=(19,), font=font,key='-TEXT-'), sg.Input(size=(8,1),justification='r',font=font,do_not_clear=False, key=layout_text[3]),sg.Text('years', justification='l', size=(12,1),font=font, key='-TEXT-')],
            [sg.Text(layout_text[4], justification='r', size=(19,), font=font,key='-TEXT-'), sg.Input(size=(8,1),justification='r',font=font,do_not_clear=False, key=layout_text[4]),sg.Text(' %', justification='l', size=(12,1), font=font,key='-TEXT-')],
            [sg.Text(layout_text[5], justification='r', size=(19,), font=font,key='-TEXT-'), sg.Input(size=(8,1),justification='r',font=font,do_not_clear=False, key=layout_text[5]),sg.Text(' %', justification='l', size=(12,1), font=font,key='-TEXT-')],
            [sg.Text(layout_text[6], justification='r', size=(19,), font=font,key='-TEXT-'), sg.Input(size=(8,1),justification='r',font=font,do_not_clear=False, key=layout_text[6]),sg.Text(' %', justification='l', size=(12,1), font=font,key='-TEXT-')],
            [sg.Button('Enter', bind_return_key=True), sg.Button('Exit')]  ]

window = sg.Window('Mortgage Calculator', layout,size=(400,400),resizable=True,element_justification='center')

counter = 0
stuff_entered = []
while True:             # Event Loop
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Enter':
        #print(values.keys())
        homeValue = values[layout_text[0]]
        downPayment = values[layout_text[1]]
        annualInterestRate = values[layout_text[2]]
        loanTerm = values[layout_text[3]]
        n_years = values[layout_text[4]]
        annual_property_tax = values[layout_text[5]]
        #monthly_payment = 
        print(homeValue)
        stuff_entered.append(values.values())
        if counter > 2:
            break
        #window['-TEXT-'].update(f'Input Value {counter+1}')
        counter += 1

window.close()
sg.popup(f'You entered {stuff_entered}')
