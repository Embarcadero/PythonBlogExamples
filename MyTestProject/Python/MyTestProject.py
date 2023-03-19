from delphifmx import *
from TestUnit import TestForm

def main():
    Application.Initialize()
    Application.Title = 'MyTestProject'
    Application.MainForm = TestForm(Application)
    Application.MainForm.Show()
    Application.Run()
    Application.MainForm.Destroy()

if __name__ == '__main__':
    main()
