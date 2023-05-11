import os
from delphifmx import *

class Length(Form):

    def __init__(self, owner):
        self.FromValue = None
        self.UnitFromLabel = None
        self.ValueFromLabel = None
        self.Title = None
        self.FromLabel = None
        self.ToLabel = None
        self.Convert = None
        self.FromUnit = None
        self.ToUnit = None
        self.ToValue = None
        self.UnitToLabel = None
        self.ValueToLabel = None
        self.BackButton = None
        self.Status = None
        self.LoadProps(os.path.join(os.path.dirname(os.path.abspath(__file__)), "LengthForm.pyfmx"))


        # Addtional initializations
        # Dictionary that gives us the relationship between units
        self.data = {
            "meter":{"meter":1, "kilometer":1/1000, "centimeter":100, "millimeter":1000, "yard":1.094, "foot":3.281, "inch":39.37, "mile":1/1609},
            "kilometer":{"meter":1000, "kilometer":1, "centimeter":100000, "millimeter":1000000, "yard":1094, "foot":3281, "inch":39370, "mile":1.609},
            "centimeter":{"meter":1/100, "kilometer":1/100000, "centimeter":1, "millimeter":10, "yard":1/91.44, "foot":1/30.48, "inch":1/2.54, "mile":1/160900},
            "millimeter":{"meter":1/1000, "kilometer":1/1000000, "centimeter":1/10, "millimeter":1, "yard":1/914.4, "foot":1/304.8, "inch":1/25.4, "mile":1/1609000},
            "yard":{"meter":1/1.094, "kilometer":1/1094, "centimeter":91.44, "millimeter":914.4, "yard":1, "foot":3, "inch":36, "mile":1/1760},
            "foot":{"meter":1/3.281, "kilometer":1/3281, "centimeter":30.48, "millimeter":304.8, "yard":1/3, "foot":1, "inch":12, "mile":1/5280},
            "inch":{"meter":1/39.37, "kilometer":1/39370, "centimeter":2.54, "millimeter":25.4, "yard":1/36, "foot":1/12, "inch":1, "mile":1/63360},
            "mile":{"meter":1609, "kilometer":1.609, "centimeter":160900, "millimeter":1609000, "yard":1760, "foot":5280, "inch":63360, "mile":1}
        }

        # Load the currencies in key values of the self.data dictionary into the FromCurrency and ToCurrency combo boxes
        for key in self.data.keys():
            self.FromUnit.Items.append(key)
            self.ToUnit.Items.append(key)

        self.Status.Text = ""

    def ConvertClick(self, Sender):
        if self.FromUnit.Selected!=None and self.ToUnit.Selected!=None and self.FromValue.Text!="": # Checking is all required fields filles
            given = self.FromUnit.Selected.Text
            to = self.ToUnit.Selected.Text
            amountGiven = int(self.FromValue.Text)
            amountCalculated  = self.data[given][to] * amountGiven
            if len(str(amountCalculated)) > 8: # If the value is longer than 8 digits then use scientific notation
                amountCalculated = '{:.3e}'.format(amountCalculated)
            self.ToValue.Text = amountCalculated
            self.Status.Text = "" # Reset status since conversion was successful (incase there was an alert earlier)
        else:
            self.Status.Text = "Please fill all relevant inputs!"
    def BackButtonClick(self, Sender):
        Application.MainForm.Show()
        self.Destroy()