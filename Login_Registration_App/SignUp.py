import os
from delphifmx import *
from sqlalchemy import create_engine

# establish connections - create new file db and connect of connect if it already exists
engine = create_engine(
	'sqlite:///users.db')

class Form2(Form):

    def __init__(self, owner):
        self.Register = None
        self.FnameText = None
        self.Fname = None
        self.LNameText = None
        self.LName = None
        self.EmailText = None
        self.Email = None
        self.PasswordText = None
        self.Password = None
        self.CPasswordText = None
        self.CPassword = None
        self.Signup = None
        self.Error = None
        self.LoadProps(os.path.join(os.path.dirname(os.path.abspath(__file__)), "SignUp.pyfmx"))

    def SignupClick(self, Sender):
        if self.FnameText.Text == "" or self.LNameText.Text == "" or self.EmailText.Text == "" or self.PasswordText.Text == "" or self.CPasswordText.Text == "":
            self.Error.Text = "Incomplete details!"
        elif self.CPasswordText.Text != self.PasswordText.Text:
            self.Error.Text = "Passwords do not match!"
        else:            
            query = "INSERT INTO users VALUES ('{}', '{}','{}', '{}')".format(self.EmailText.Text, self.FnameText.Text, self.LNameText.Text, self.PasswordText.Text)

            # execute the insert record statement
            engine.execute(query)

            self.Error.Text = "Successful SignUp"