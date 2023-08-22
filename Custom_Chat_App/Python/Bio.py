import os
from delphifmx import *
# Import chat form
from Chat import ChatScreen


class BioScreen(Form):

    def __init__(self, owner):
        self.TitleLabel = None
        self.AgeLabel = None
        self.NameLabel = None
        self.AgeNumberBox = None
        self.NameEdit = None
        self.Image1 = None
        self.StartButton = None
        self.StyleBook1 = None
        self.LoadProps(os.path.join(os.path.dirname(
            os.path.abspath(__file__)), "Bio.pyfmx"))

    def StartButtonClick(self, Sender):
        chat = ChatScreen(self, name=self.NameEdit.Text,
                          age=self.AgeNumberBox.Text)
        chat.Show()
