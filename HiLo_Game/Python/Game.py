import os
from delphifmx import *
import random

class GameForm(Form):

    def __init__(self, owner):
        self.ScoreLabel = None
        self.Number = None
        self.HighButton = None
        self.LowButton = None
        self.AgainButton = None
        self.StatusLabel = None
        self.LoadProps(os.path.join(os.path.dirname(os.path.abspath(__file__)), "Game.pyfmx"))

        # Additional initializations
        self.Score = 0
        self.GuessNumber = random.randint(0, 10)  # Generate a random number between 0 and 10
        self.Number.Text = str(self.GuessNumber)

    def __UpdateGame(self, compare):
        self.StatusLabel.Text = ""  # Clear the status label each time button clicked
        prev = self.GuessNumber  # Store the guess number
        self.GuessNumber = random.randint(0, 10)  # Generate a new random number within a range
        self.Number.Text = str(self.GuessNumber)
        if compare==">" and prev > self.GuessNumber: # If the player guessed lower and the new number is actually lower
            self.StatusLabel.Text = "That's right"
            self.Score +=1  # Increment the score
            self.ScoreLabel.Text = "Score:" + str(self.Score)  
        elif compare=="<" and prev <= self.GuessNumber:  # If the player guessed higher and the new number is actually higher
            self.StatusLabel.Text = "That's right"
            self.Score +=1  # Increment the score
            self.ScoreLabel.Text = "Score:" + str(self.Score)
        else:  # If the player guessed wrong
            self.StatusLabel.Text = "GAME OVER"
            self.LowButton.Enabled = False  # Disable the low button
            self.HighButton.Enabled = False  # Disable the high button
            self.AgainButton.Enabled = True  # Enable the again button

    def HighButtonClick(self, Sender):
        self.__UpdateGame("<")  # If the high button is clicked, update the game

    def LowButtonClick(self, Sender):
        self.__UpdateGame(">")  # If the low button is clicked, update the game

    def AgainButtonClick(self, Sender):
        self.Score = 0  # Reset the score to 0
        self.ScoreLabel.Text = "Score:" + str(self.Score)  # Update the score label
        self.GuessNumber = random.randint(0, 10)  # Generate a new random number between 0 and 10
        self.Number.Text = str(self.GuessNumber)  
        self.LowButton.Enabled = True  # Enable the low button
        self.HighButton.Enabled = True  # Enable the high button
        self.AgainButton.Enabled = False  # disable the again button
        self.StatusLabel.Text = ""  # Clear the status label