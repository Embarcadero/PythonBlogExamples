import os
from delphifmx import *

class Time(Form):

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
        self.LoadProps(os.path.join(os.path.dirname(os.path.abspath(__file__)), "TimeForm.pyfmx"))

        # Addtional initializations
        # Dictionary that gives us the relationship between units
        self.data = {
            "second":{"second":1, "millisecond":1000, "minute":1/60, "hour":1/3600, "day":1/86400, "week":1/6084800, "month":1/2628000, "year":1/31540000},
            "millisecond":{"second":1/1000, "millisecond":1, "minute":1/60000, "hour":1/3600000, "day":1/86400000, "week":1/6084800000, "month":1/2628000000, "year":1/31540000000},
            "minute":{"second":60, "millisecond":60000, "minute":1, "hour":1/60, "day":1/1440, "week":1/10080, "month":1/43800, "year":1/525600},
            "hour":{"second":3600, "millisecond":3600000, "minute":60, "hour":1, "day":1/24, "week":1/168, "month":1/730, "year":1/8760},
            "day":{"second":86400, "millisecond":86400000, "minute":1440, "hour":24, "day":1, "week":1/7, "month":1/30.417, "year":1/365},
            "week":{"second":604800, "millisecond":604800000, "minute":10080, "hour":168, "day":7, "week":1, "month":1/4.345, "year":1/52.143},
            "month":{"second":2628000, "millisecond":2628000000, "minute":43800, "hour":730, "day":30.417, "week":4.345, "month":1, "year":1/12},
            "year":{"second":31540000, "millisecond":31540000000, "minute":525600, "hour":8760, "day":365, "week":52.143, "month":12, "year":1}
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