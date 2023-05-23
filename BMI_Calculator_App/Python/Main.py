import os
from delphifmx import *
from Results import ResultsForm
class MainForm(Form):

    def __init__(self, owner):
        self.WeightEdit = None
        self.HeightFeetEdit = None
        self.ResultsButton = None
        self.HeightLabel = None
        self.WeightLabel = None
        self.Title = None
        self.PoundsRadio = None
        self.KgRadio = None
        self.FeetLabel = None
        self.HeightInchEdit = None
        self.InchLabel = None
        self.Status = None
        self.LoadProps(os.path.join(os.path.dirname(os.path.abspath(__file__)), "Main.pyfmx"))

        self.BMI = 0 # Initialize BMI that would be calculated and sent to next form

    def ResultsButtonClick(self, Sender):
        # Error Handling
        if (self.PoundsRadio==False and self.KgRadio==False) or self.HeightFeetEdit.Text=="" or self.HeightInchEdit.Text=="" or self.WeightEdit.Text=="":
            self.Status.Text = "Please fill in all fields"
        elif int(self.HeightInchEdit.Text) < 0 or int(self.HeightInchEdit.Text) > 11:
            self.Status.Text = "Give inches between 0 and 11"
        # If no errors
        else:
            self.BMI = self.GetBMI(float(self.WeightEdit.Text), int(self.HeightFeetEdit.Text), int(self.HeightInchEdit.Text))
            self.results = ResultsForm(self, BMI=self.BMI)
            self.results.Show()

    def GetBMI(self, weight, heightft, heightin):
        # For BMI Calculation, Weight should be in kg and Height in meters
        if self.PoundsRadio.IsChecked:
            weight = weight / 2.205
        height = heightft * 0.3048 + heightin * 0.0254 # Conversion to meters
        bmi = round(weight / (height**2), 2) # BMI = Weight/ (Height)^2
        return bmi
