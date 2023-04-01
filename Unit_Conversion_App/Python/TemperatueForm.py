import os
from delphifmx import *

class Temperature(Form):

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
        self.LoadProps(os.path.join(os.path.dirname(os.path.abspath(__file__)), "TemperatueForm.pyfmx"))

        # Addtional initializations
        # Dictionary that gives us the relationship between units using lamda functions
        self.data = {
            "celsius":{"celsius":lambda a: a, "kelvin":lambda a: a+273.15, "fahrenheit":lambda a: a*(9/5)+32},
            "kelvin":{"celsius":lambda a: a-273.15, "kelvin":lambda a: a, "fahrenheit":lambda a: (a-273.15)*(9/5)+32},
            "fahrenheit":{"celsius":lambda a: (a-32)*(5/9), "kelvin":lambda a: (a-32)*(5/9)+273.15, "fahrenheit":lambda a: a}                
        }

        # Load the currencies in key values of the self.data dictionary into the FromCurrency and ToCurrency combo boxes
        for key in self.data.keys():
            self.FromUnit.Items.append(key)
            self.ToUnit.Items.append(key)

        self.Status.Text = ""

    def ConvertClick(self, Sender):
        if self.FromUnit.Selected!=None and self.ToUnit.Selected!=None and self.FromValue.Text!="":
            given = self.FromUnit.Selected.Text
            to = self.ToUnit.Selected.Text
            amountGiven = int(self.FromValue.Text)
            amountCalculated  = self.data[given][to](amountGiven) # using the lambda 
            if len(str(amountCalculated)) > 8: # if the value is longer than 8 digits then use scientific notation
                amountCalculated = '{:.3e}'.format(amountCalculated)
            self.ToValue.Text = amountCalculated
            self.Status.Text = "" # reset status since conversion was successful (incase there was an alert earlier) 
        else: 
            self.Status.Text = "Please fill all relevant inputs!"        
        
    def BackButtonClick(self, Sender):
        self.Destroy()
        Application.MainForm.Show()