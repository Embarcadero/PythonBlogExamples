import os
from delphifmx import *

class CurrencyConverterApp(Form):

    def __init__(self, owner):
        self.data = {
                "USD":{"EUR":0.96, "CAD":1.34, "CHF":0.95, "GBP":0.84, "OMR":0.39, "GIP":0.85, "KYD":0.84, "JOD":0.71, "BHD":0.38, "KWD":0.31},
                "EUR":{"USD":1.04, "CAD":1.39, "CHF":0.98, "GBP":0.87, "OMR":0.40, "GIP":0.87, "KYD":0.87, "JOD":0.74, "BHD":0.36, "KWD":0.32},
                "CAD":{"EUR":0.72, "USD":0.75, "CHF":0.71, "GBP":0.63, "OMR":0.29, "GIP":0.64, "KYD":0.63, "JOD":0.53, "BHD":0.28, "KWD":0.23},
                "CHF":{"EUR":1.02, "CAD":1.41, "USD":1.06, "GBP":0.89, "OMR":0.41, "GIP":0.90, "KYD":0.88, "JOD":0.75, "BHD":0.40, "KWD":0.33},
                "GBP":{"EUR":1.15, "CAD":1.59, "CHF":1.13, "USD":1.19, "OMR":0.46, "GIP":1.00, "KYD":1.00, "JOD":0.84, "BHD":0.45, "KWD":0.37},
                "OMR":{"EUR":2.50, "CAD":3.47, "CHF":2.46, "GBP":2.18, "USD":2.60, "GIP":2.32, "KYD":2.17, "JOD":1.84, "BHD":0.98, "KWD":0.80},
                "GIP":{"EUR":1.15, "CAD":1.59, "CHF":1.13, "USD":1.19, "OMR":0.46, "GBP":1.00, "KYD":1.00, "JOD":0.84, "BHD":0.45, "KWD":0.37},
                "KYD":{"EUR":1.15, "CAD":1.59, "CHF":1.13, "USD":1.19, "OMR":0.46, "GIP":1.00, "GBP":1.00, "JOD":0.84, "BHD":0.45, "KWD":0.37},
                "JOD":{"EUR":1.36, "CAD":1.88, "CHF":1.33, "GBP":1.19, "OMR":0.45, "GIP":1.19, "KYD":0.43, "USD":1.41, "BHD":0.53, "KWD":0.43},
                "BHD":{"EUR":2.56, "CAD":3.54, "CHF":2.51, "GBP":2.23, "OMR":1.02, "GIP":2.24, "KYD":0.82, "JOD":1.88, "USD":2.65, "KWD":0.82},
                "KWD":{"EUR":3.13, "CAD":4.34, "CHF":3.07, "GBP":2.73, "OMR":1.25, "GIP":2.73, "KYD":2.72, "JOD":2.30, "BHD":1.22, "USD":3.25}
            } # Currency conversion data recorded on 7th Nov 2022
        self.FromAmount = None
        self.Currency1 = None
        self.Amount1 = None
        self.Currency2 = None
        self.Amount2 = None
        self.Title = None
        self.FromLabel = None
        self.ToLabel = None
        self.Convert = None
        self.FromCurrency = None
        self.ToCurrency = None
        self.ToAmount = None
        self.LoadProps(os.path.join(os.path.dirname(os.path.abspath(__file__)), "CurrencyConverter.pyfmx"))

        # Load the currencies in key values of the self.data dictionary into the FromCurrency and ToCurrency combo boxes
        for key in self.data.keys():
            self.FromCurrency.Items.append(key)
            self.ToCurrency.Items.append(key)

    def ConvertClick(self, Sender):
        given = self.FromCurrency.Selected.Text
        to = self.ToCurrency.Selected.Text
        amountGiven = int(self.FromAmount.Text)
        amountCalculated  = self.data[given][to] * amountGiven
        self.ToAmount.Text = round(amountCalculated, 2)