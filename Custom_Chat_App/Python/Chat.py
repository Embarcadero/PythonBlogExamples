import os
from delphifmx import *
# More required imports
from LLMChat import LLM


class ChatScreen(Form):

    def __init__(self, owner, name, age):
        self.SendButton = None
        self.UserQsEdit = None
        self.Header = None
        self.HeaderLabel = None
        self.Footer = None
        self.BackButton = None
        self.ChatMemo = None
        self.StyleBook1 = None
        self.LoadProps(os.path.join(os.path.dirname(
            os.path.abspath(__file__)), "Chat.pyfmx"))

        self.HeaderLabel.Text = "{}'s Chat".format(name)
        self.age = age
        self.name = name
        self.llm = LLM(name, age)  # Create LLM chain instance

    def SendButtonClick(self, Sender):
        # Add user's question to the memo for chat history
        self.ChatMemo.Lines.Add("{}: {}".format(
            self.name, self.UserQsEdit.Text))
        # Get the reponse to the question
        reply = self.llm.getReply(self.UserQsEdit.Text)
        # Add the response to the memo as well
        self.ChatMemo.Lines.Add("Chatbot:{}".format(reply))

    def BackButtonClick(self, Sender):
        self.Destroy()
import os
from delphifmx import *
# More required imports
from LLMChat import LLM


class ChatScreen(Form):

    def __init__(self, owner, name, age):
        self.SendButton = None
        self.UserQsEdit = None
        self.Header = None
        self.HeaderLabel = None
        self.Footer = None
        self.BackButton = None
        self.ChatMemo = None
        self.StyleBook1 = None
        self.LoadProps(os.path.join(os.path.dirname(
            os.path.abspath(__file__)), "Chat.pyfmx"))

        self.HeaderLabel.Text = "{}'s Chat".format(name)
        self.age = age
        self.name = name
        self.llm = LLM(name, age)  # Create LLM chain instance

    def SendButtonClick(self, Sender):
        # Add user's question to the memo for chat history
        self.ChatMemo.Lines.Add("{}: {}".format(
            self.name, self.UserQsEdit.Text))
        # Get the reponse to the question
        reply = self.llm.getReply(self.UserQsEdit.Text)
        # Add the response to the memo as well
        self.ChatMemo.Lines.Add("Chatbot:{}".format(reply))

    def BackButtonClick(self, Sender):
        self.Destroy()
