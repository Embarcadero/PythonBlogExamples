import os
from delphifmx import *

class ResultsForm(Form):

    def __init__(self, owner, BMI):
        self.BMIScore = None
        self.Label1 = None
        self.DetailsLabel = None
        self.CategoryLabel = None
        self.Title = None
        self.Reset = None
        self.LoadProps(os.path.join(os.path.dirname(os.path.abspath(__file__)), "Results.pyfmx"))
        
        # More initializations
        self.BMIScore.Text = str(BMI)
        self.BMI = BMI
        self.Detail = {
            "Underweight": "Your BMI indicates that you are underweight, which may increase your risk of health problems. You should consult a doctor or a dietitian to develop a healthy eating plan that can help you gain weight in a safe and sustainable way.",
            "Healthy": "Your BMI indicates that you are in a healthy weight range, which is great for your overall health and well-being. Keep up the good work by staying physically active and eating a balanced diet.",
            "Overweight": "Your BMI indicates that you are overweight, which may increase your risk of health problems such as heart disease and diabetes. You should consider making lifestyle changes such as increasing your physical activity and reducing your calorie intake.",
            "Obese":"Your BMI indicates that you are obese, which significantly increases your risk of health problems such as heart disease, stroke, and cancer. You should consult a dietitian to develop a weight loss plan that can help you achieve a healthy weight and reduce your risk of these health problems.",
            }

        # Categorization according to BMI
        if BMI < 18.5:
            self.CategoryLabel.Text = "Underweight"
        elif 18.5 < BMI < 24.9:
            self.CategoryLabel.Text = "Healthy"
        elif 25.0 < BMI < 29.9:
            self.CategoryLabel.Text = "Overweight"
        elif BMI > 30:
            self.CategoryLabel.Text = "Obese"

        self.DetailsLabel.Text = self.Detail[self.CategoryLabel.Text] # Display details and suggestions according to the category
