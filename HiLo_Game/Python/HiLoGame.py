from delphifmx import *
from MainMenu import MainForm

def main():
    Application.Initialize()
    Application.Title = 'HiLoGame'
    Application.MainForm = MainForm(Application)
    Application.MainForm.Show()
    Application.Run()
    Application.MainForm.Destroy()

if __name__ == '__main__':
    main()
