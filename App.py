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