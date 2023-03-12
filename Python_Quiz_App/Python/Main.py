import os
from delphifmx import *
from Quiz import QuizForm

class MainForm(Form):

    def __init__(self, owner):
        self.Title = None
        self.Start = None
        self.LoadProps(os.path.join(os.path.dirname(os.path.abspath(__file__)), "Main.pyfmx"))

        self.Score = 0 # Initialize quiz score
        self.QuestionNumber = 1 # Initialize question number

    def StartClick(self, Sender):
        self.QuestionWindow = QuizForm(self, QuestionNumber=self.QuestionNumber, Score=self.Score) # Create question 1 window
        self.QuestionWindow.show()