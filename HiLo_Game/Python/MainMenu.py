import os
from delphifmx import *
from Game import GameForm


class MainForm(Form):
    def __init__(self, owner):
        self.Title = None
        self.Rules = None
        self.Start = None
        self.LoadProps(
            os.path.join(os.path.dirname(os.path.abspath(__file__)), "MainMenu.pyfmx")
        )

        self.Rules.Text = """Rules: \nThe rules for the game are simple.
The game will generate a random number between 1 and 10.
Your job will be to predict whether the next number will be higher or lower than the current number.
        """

    def StartClick(self, Sender):
        Game = GameForm(self)
        Game.Show()