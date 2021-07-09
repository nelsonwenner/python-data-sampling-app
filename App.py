from SerialCommands import SerialCommands
from SocketCommands import SocketCommands
from time import perf_counter
import PySimpleGUI as sg
import threading
import datetime
import queue
import csv
import re

class App:

  header_font = ('Courier', 16, 'bold')
  large_font = ('Courier', 12)
  medium_font = ('Courier', 10)
  small_font = ('Courier', 8)

  sg.SetOptions(
    background_color='#2C2C2C',
    text_element_background_color='#2C2C2C',
    element_background_color='#2C2C2C',
    scrollbar_color=None,
    input_elements_background_color='#FAFAFA',
    progress_meter_color=('#32D957', '#EEEEEE'),
    button_color=('#FAFAFA', '#222222')
  )

  layout = [
    [
      sg.Text('Data Sampling App', justification='center', 
      pad=((55, 0), (10, 15)), font=header_font)
    ],
    [
      sg.Checkbox('Wifi', key='_WIFI_', change_submits=True, 
      font=large_font, pad=((72, 5), (0, 0))), 
      sg.VerticalSeparator(), 
      sg.Checkbox('Serial', key='_SERIAL_', change_submits=True,
      default=True, font=large_font, pad=((0, 0), (0, 0)))
    ],
    [
      sg.Text('Select your serial port', pad=((68, 0), (20, 10)), 
      key='_DEVICE_TITLE_', font=medium_font)
    ],
    [
      sg.Listbox(values=[x[0] for x in SerialCommands.get_ports()],
      size=(40, 6), key='_DEVICE_LIST_', font=medium_font, enable_events=True)
    ],
    [
      sg.Text('', key='_SERIAL_PORT_CONFIRM_', size=(40, 1), font=small_font)
    ],
    [
      sg.Text('How many samples?', font=medium_font, ),
      sg.VerticalSeparator(), sg.Input(do_not_clear=True, enable_events=True, 
      key='_SAMPLE_IN_', font=medium_font)
    ],
    [
      sg.HorizontalSeparator()
    ],
    [
      sg.Text('Status:', font=medium_font, pad=((0, 0), (0, 0))),
      sg.Text('', key='_OUTPUT_', size=(40, 2), font=medium_font, pad=((0, 0), (17, 0))) 
    ],
    [
      sg.Button('Start',  key='_ACT_BUTTON_', font=medium_font, size=(40, 1), 
      pad=((0, 0), (0, 0)))
    ],
    [
      sg.Text('NelsonWenner - Version: 0.1', justification='right', size=(60, 1), 
      pad=((0, 0), (10, 0)), font=small_font) 
    ]
  ]

  def __init__(self):
    self.window = sg.Window('', self.layout, size=(360, 430), keep_on_top=True)

    while True:
      event, values = self.window.Read(timeout=100)

      if event == sg.WIN_CLOSED: break

    self.window.close()

if __name__ == '__main__':
  App()