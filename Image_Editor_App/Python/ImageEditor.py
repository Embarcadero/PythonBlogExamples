from delphifmx import *
from Main import MainFrom

def main():
    Application.Initialize()
    Application.Title = 'Image Editor App'
    Application.MainForm = MainFrom(Application)
    Application.MainForm.Show()
    Application.Run()
    Application.MainForm.Destroy()

if __name__ == '__main__':
    main()
