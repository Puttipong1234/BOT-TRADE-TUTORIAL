import requests

import PySimpleGUI as sg

from app import SM , SM_t

sg.theme('Default1')

layout = [
 [sg.Frame('', layout = [
   [sg.T('PYBOTT - AUTOBINANCE TRADER V1.0.0',size=(50,1), key='label')],
   [sg.T('YOUR BINANCE API KEY')],
   [sg.I('',key='-APIKEY-')],
   [sg.T('YOUR BINANCE API SECRET')],
   [sg.I('',key='-APISECRET-')],
   [sg.T('YOUR PYBOTT REFERRAL CODE')],
   [sg.I('',key='-REFCODE-')],
   [sg.T('YOUR EMAIL ADDRESS')],
   [sg.I('',key='-EMAIL-')],
   [sg.B('START TRADING : เทรดเลย!!', key='STARTTRADING')],
   [sg.B('STOP TRADING : หยุดการเทรด!!', key='STOPTRADING')],
   [sg.T('PLEASE CONTACT  PYBOTT FACEBOOK FOR MORE INFORMATION ')]
])]]

window = sg.Window('App', layout)

if __name__ == '__main__':
    while True:
        event, values = window.read()
        if event in (None, 'Exit'):
            break
        
        if event == '':
            pass
        
        if event == 'label':
            pass

        if event == 'lineEdit':
            pass

        if event == 'STARTTRADING':
            requests.post(url="https://bottrade-tutorial.herokuapp.com/START")
        
        if event == 'STOPTRADING':
            requests.post(url="https://bottrade-tutorial.herokuapp.com/STOP")
            
            
    window.close()

    