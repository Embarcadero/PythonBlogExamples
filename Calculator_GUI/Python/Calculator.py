import os
from delphifmx import *

class CalculatorGUI(Form):
    def __init__(self, owner):
        self.Del = None
        self.C = None
        self.Percent = None
        self.Plus = None
        self.Seven = None
        self.Eight = None
        self.Nine = None
        self.Minus = None
        self.Four = None
        self.Five = None
        self.Six = None
        self.Multiply = None
        self.One = None
        self.Two = None
        self.Three = None
        self.Zero = None
        self.Dot = None
        self.Divide = None
        self.Equals = None
        self.Calc = None
        self.Results = None
        self.LoadProps(os.path.join(os.path.dirname(os.path.abspath(__file__)), "Calculator.pyfmx"))
        self.Calculation = ""
        self.Results.Text = ""
        self.Calc.Text = ""

    def DelClick(self, Sender):
        self.Calculation = self.Calculation[:-1]
        self.Calc.Text = self.Calculation

    def CClick(self, Sender):
        self.Calculation = ""
        self.Calc.Text = self.Calculation
        self.Results.Text = ""

    def PercentClick(self, Sender):
        self.Calculation += "%"
        self.Calc.Text = self.Calculation

    def PlusClick(self, Sender):
        self.Calculation += "+"
        self.Calc.Text = self.Calculation

    def SevenClick(self, Sender):
        self.Calculation += "7"
        self.Calc.Text = self.Calculation

    def EightClick(self, Sender):
        self.Calculation += "8"
        self.Calc.Text = self.Calculation

    def NineClick(self, Sender):
        self.Calculation += "9"
        self.Calc.Text = self.Calculation

    def MinusClick(self, Sender):
        self.Calculation += "-"
        self.Calc.Text = self.Calculation

    def FourClick(self, Sender):
        self.Calculation += "4"
        self.Calc.Text = self.Calculation

    def FiveClick(self, Sender):
        self.Calculation += "5"
        self.Calc.Text = self.Calculation

    def SixClick(self, Sender):
        self.Calculation += "6"
        self.Calc.Text = self.Calculation

    def MultiplyClick(self, Sender):
        self.Calculation += "*"
        self.Calc.Text = self.Calculation

    def OneClick(self, Sender):
        self.Calculation += "1"
        self.Calc.Text = self.Calculation

    def TwoClick(self, Sender):
        self.Calculation += "2"
        self.Calc.Text = self.Calculation

    def ThreeClick(self, Sender):
        self.Calculation += "3"
        self.Calc.Text = self.Calculation

    def ZeroClick(self, Sender):
        self.Calculation += "0"
        self.Calc.Text = self.Calculation

    def DotClick(self, Sender):
        self.Calculation += "."
        self.Calc.Text = self.Calculation

    def DivideClick(self, Sender):
        self.Calculation += "/"
        self.Calc.Text = self.Calculation

    def EqualsClick(self, Sender):
        try:
            self.Results.Text = str(eval(self.Calculation))
        except:
            self.Results.Text = "Error"