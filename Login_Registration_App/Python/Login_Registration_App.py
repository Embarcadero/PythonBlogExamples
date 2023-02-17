from delphifmx import *
from SignIn import Form3

def main():
    Application.Initialize()
    Application.Title = 'Login_Registration_App'
    Application.MainForm = Form3(Application)
    Application.MainForm.Show()
    Application.Run()
    Application.MainForm.Destroy()

if __name__ == '__main__':
    main()