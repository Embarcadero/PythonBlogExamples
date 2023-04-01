import os
from delphifmx import *

# Extra Imports
from Stopwatch import StopwatchForm
from Timer import TimerForm

class MainForm(Form):

    def __init__(self, owner):
        self.Title = None
        self.StopwatchFormButton = None
        self.TimerFormButton = None
        self.LoadProps(os.path.join(os.path.dirname(os.path.abspath(__file__)), "MainMenu.pyfmx"))

    def StopwatchFormButtonClick(self, Sender):
        self.StopwatchWindow = StopwatchForm(self)
        self.StopwatchWindow.Show()

    def TimerFormButtonClick(self, Sender):
        self.TimerWindow = TimerForm(self)
        self.TimerWindow.Show()