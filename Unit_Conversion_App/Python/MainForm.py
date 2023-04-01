import os
from delphifmx import *
# Additional imports
from LengthForm import Length
from TemperatueForm import Temperature
from TimeForm import Time
from WeightForm import Weight

class Main(Form):

    def __init__(self, owner):
        self.Title = None
        self.TemperatureFromButton = None
        self.LengthFormButton = None
        self.WeightFromButton = None
        self.TimeFormButton = None
        self.LoadProps(os.path.join(os.path.dirname(os.path.abspath(__file__)), "MainForm.pyfmx"))

    def TemperatureFromButtonClick(self, Sender):
        self.TempForm = Temperature(self)
        self.TempForm.Show()

    def LengthFormButtonClick(self, Sender):
        self.LengthForm = Length(self)
        self.LengthForm.Show()

    def WeightFromButtonClick(self, Sender):
        self.WeightForm = Weight(self)
        self.WeightForm.Show()

    def TimeFormButtonClick(self, Sender):
        self.TimeForm = Time(self)
        self.TimeForm.Show()