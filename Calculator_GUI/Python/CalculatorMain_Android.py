from delphifmx import *
from Calculator import CalculatorGUI

def main():
    Application.MainForm = CalculatorGUI(Application)
    Application.MainForm.Show()

if __name__ == '__main__':
    main()