import os
from delphifmx import *
# Additional imports
import random


class GameForm(Form):

    def __init__(self, owner):
        self.Button1 = None
        self.Button2 = None
        self.Button3 = None
        self.Button4 = None
        self.Button5 = None
        self.Button6 = None
        self.Button7 = None
        self.Button8 = None
        self.Button9 = None
        self.Button10 = None
        self.ScoreLabel = None
        self.Card1Label = None
        self.Card2Label = None
        self.Status = None
        self.BackButton = None
        self.ResetButton = None
        self.TriesLabel = None
        self.LoadProps(os.path.join(os.path.dirname(
            os.path.abspath(__file__)), "Game.pyfmx"))

        # Randomly assign values to all cards at the start
        self.__RandomizeCards()

        self.prev = (self.Button1, "")  # Store the first selected card data
        self.score = 0  # Game score counter
        self.tries = 0  # Tries counter
        self.flag = 0  # Flag to check if one complete try/guess has been made

    def __RandomizeCards(self):
        # Define the keys for the dictionary
        keys = ["Button1", "Button2", "Button3", "Button4", "Button5",
                "Button6", "Button7", "Button8", "Button9", "Button10"]

        # Define the values to randomly select from
        values = ["A", "A", "B", "B", "C", "C", "D", "D", "E", "E"]

        # Shuffle the values randomly
        random.shuffle(values)

        # Create the dictionary
        self.d = dict(zip(keys, values))

    def __Functionality(self, Button, name):
        val = self.d[name]  # Get value against this button

        # If one complete try has been done
        if self.flag == 1:
            self.tries += 1  # Then increase tries counter
            self.TriesLabel.Text = "Tries: "+str(self.tries)
            self.flag = 0  # Reset tires flag

            # If the two cards/buttons selected are the same
            if self.prev[1] == val:
                self.score += 1  # Then increase score counter
                self.ScoreLabel.Text = "Score: "+str(self.score)
                Button.Text = val  # Show the value behind
                Button.Enabled = False  # Disable the cards/buttons so that they cannot be clicked
                self.prev[0].Enabled = False

                # If score is 5 then all the cards/buttons have been matched
                if self.score == 5:
                    self.Status.Text = "You Win!"
                    self.ResetButton.Enabled = True  # Now reset button can be clicked

            # If the two cards/buttons selected are not the same
            else:
                # Show the respective values below the cards
                self.Card1Label.Text = "Card 1: " + self.prev[1]
                self.Card2Label.Text = "Card 2: " + val
                Button.Text = val
                Button.Text = "?"  # Hide the cards again0
                self.prev[0].Text = "?"

        # If just one card/button has been selected and
        # the other has to be selected to complete the guess
        else:
            self.Card1Label.Text = "Card 1:"
            self.Card2Label.Text = "Card 2:"
            Button.Text = val  # Show the value behind
            self.flag += 1  # Increase flag to show that first card selected from the try and one more left
            self.prev = (Button, val)  # Store this button info to compare

    # Implement this functionality when any of the 10 buttons/cards are selected
    def Button1Click(self, Sender):
        self.__Functionality(self.Button1, "Button1")

    def Button2Click(self, Sender):
        self.__Functionality(self.Button2, "Button2")

    def Button3Click(self, Sender):
        self.__Functionality(self.Button3, "Button3")

    def Button4Click(self, Sender):
        self.__Functionality(self.Button4, "Button4")

    def Button5Click(self, Sender):
        self.__Functionality(self.Button5, "Button5")

    def Button6Click(self, Sender):
        self.__Functionality(self.Button6, "Button6")

    def Button7Click(self, Sender):
        self.__Functionality(self.Button7, "Button7")

    def Button8Click(self, Sender):
        self.__Functionality(self.Button8, "Button8")

    def Button9Click(self, Sender):
        self.__Functionality(self.Button9, "Button9")

    def Button10Click(self, Sender):
        self.__Functionality(self.Button10, "Button10")

    # Go back to the main screen
    def BackButtonClick(self, Sender):
        self.Destroy()

    # Play game again so bring back to initial state
    def ResetButtonClick(self, Sender):
        # Randomize the card/button values and reset all labels
        self.__RandomizeCards()
        self.prev = (self.Button1, "")
        self.score = 0
        self.tries = 0
        self.flag = 0
        self.TriesLabel.Text = "Tries: "
        self.ScoreLabel.Text = "Score: "
        self.Status.Text = ""
        self.ResetButton.Enabled = False

        # Hide all cards/buttons (so show ?) and enable them so that they can be clicked
        Buttons = [self.Button1, self.Button2, self.Button3, self.Button4, self.Button5,
                   self.Button6, self.Button7, self.Button8, self.Button9, self.Button10]
        for Button in Buttons:
            Button.Text = "?"
            Button.Enabled = True
