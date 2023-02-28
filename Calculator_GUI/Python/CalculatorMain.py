from delphifmx import *
from Calculator import CalculatorGUI

def main():
    Application.Initialize()
    Application.Title = 'CalculatorGUI'
    Application.MainForm = CalculatorGUI(Application)
    Application.MainForm.Show()
    Application.Run()
    Application.MainForm.Destroy()

if __name__ == '__main__':
    main()
