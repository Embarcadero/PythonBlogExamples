import os
from delphifmx import *

class ResultsForm(Form):

    def __init__(self, owner, Score):
        self.Score = None
        self.Level = None      
        self.ResultLabel = None
        self.LoadProps(os.path.join(os.path.dirname(os.path.abspath(__file__)), "Results.pyfmx"))
        
        self.Score.Text = "Score: " + str(Score) # Display score out of ten

        # Display level, based on score
        if Score < 6:
            self.Level.Text += " Novice"
        elif Score < 9:
            self.Level.Text += " Intermediate"
        else:
            self.Level.Text += " Expert" 