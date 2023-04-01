from delphifmx import *
from MainForm import Main

def main():
    Application.Initialize()
    Application.Title = 'UnitConversionApp'
    Application.MainForm = Main(Application)
    Application.MainForm.Show()
    Application.Run()
    Application.MainForm.Destroy()

if __name__ == '__main__':
    main()
