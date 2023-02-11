from delphifmx import *
from CurrencyConverter import CurrencyConverterApp

def main():
    Application.Initialize()
    Application.Title = 'CurrencyConverter'
    Application.MainForm = CurrencyConverterApp(Application)
    Application.MainForm.Show()
    Application.Run()
    Application.MainForm.Destroy()

if __name__ == '__main__':
    main()
