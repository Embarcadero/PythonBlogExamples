import os
from delphifmx import *

class Weight(Form):

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
        self.LoadProps(os.path.join(os.path.dirname(os.path.abspath(__file__)), "WeightForm.pyfmx"))

        # Addtional initializations
        # Dictionary that gives us the relationship between units
        self.data = {
            "kilogram":{"kilogram":1, "gram":1000, "milligram":1000000, "metric ton":1/1000, "pound":2.205, "ounce":35.274},
            "gram":{"kilogram":1/1000, "gram":1, "milligram":1000, "metric ton":1/1000000, "pound":1/453.6, "ounce":1/28.35},
            "milligram":{"kilogram":1/1000000, "gram":1/1000, "milligram":1, "metric ton":1/1000000000, "pound":1/453600, "ounce":1/28350},
            "metric ton":{"kilogram":1000, "gram":1000000, "milligram":1000000000, "metric ton":1, "pound":2205, "ounce":35270},
            "pound":{"kilogram":1/2.205, "gram":453.6, "milligram":453600, "metric ton":2205, "pound":1, "ounce":16},
            "ounce":{"kilogram":1/35.274, "gram":28.35, "milligram":28350, "metric ton":1/35270, "pound":1/16, "ounce":1}
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