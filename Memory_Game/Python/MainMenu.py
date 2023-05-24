import os
from delphifmx import *
from Game import GameForm

class MainForm(Form):

    def __init__(self, owner):
        self.Title = None
        self.StartButton = None
        self.LoadProps(os.path.join(os.path.dirname(os.path.abspath(__file__)), "MainMenu.pyfmx"))

    def StartButtonClick(self, Sender):
        Game = GameForm(self)
        Game.Show()