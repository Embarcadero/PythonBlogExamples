from delphifmx import *
from Main import MainForm

def main():
    Application.Initialize()
    Application.Title = 'MLFoodClassifier'
    Application.MainForm = MainForm(Application)
    Application.MainForm.Show()
    Application.Run()
    Application.MainForm.Destroy()

if __name__ == '__main__':
    main()
