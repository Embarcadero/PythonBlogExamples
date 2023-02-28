from delphifmx import *
from SignIn import SignInForm

def main():
    Application.Initialize()
    Application.Title = 'Login_Registration_App'
    Application.MainForm = SignInForm(Application)
    Application.MainForm.Show()
    Application.Run()
    Application.MainForm.Destroy()

if __name__ == '__main__':
    main()
