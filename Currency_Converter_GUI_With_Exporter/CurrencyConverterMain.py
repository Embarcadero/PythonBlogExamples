from delphifmx import *
from CurrencyConverter import CurrencyConverterApp

def main():
    Application.MainForm = CurrencyConverterApp(Application)
    Application.MainForm.Show()

if __name__ == '__main__':
    main()