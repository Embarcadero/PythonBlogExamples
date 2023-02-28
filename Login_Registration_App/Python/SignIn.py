import os
from delphifmx import *
from SignUp import SignUpForm
from sqlalchemy import create_engine, text

# establish connections - create new file db and connect of connect if it already exists
engine = create_engine(
    'sqlite:///users.db')
class SignInForm(Form):

    def __init__(self, owner):
        self.Login = None
        self.Email = None
        self.PasswordText = None
        self.Password = None
        self.Signin = None
        self.EmailText = None
        self.Status = None
        self.Signup = None
        self.LoadProps(os.path.join(os.path.dirname(os.path.abspath(__file__)), "SignIn.pyfmx"))

    def SigninClick(self, Sender):
        if self.EmailText.Text == "" or self.PasswordText.Text == "":
            self.Status.Text = "Incomplete details"
        else:
            # write the SQL query inside the text() block
            sql = text("SELECT * FROM users WHERE users.email='{}' AND users.password='{}'".format(self.EmailText.Text, self.PasswordText.Text))
            result = engine.execute(sql).fetchall()
            print(result)
            if len(result) == 0:
                self.Status.Text = "Incorrect or invalid login details"
            else:
                Fname = result[0][1]
                self.Status.Text = "Successful login. Welcome {}".format(Fname)

    def SignupClick(self, Sender):
        Application.MainForm = SignUpForm(Application)
        Application.MainForm.Show()
        Application.MainForm = SignInForm(Application)