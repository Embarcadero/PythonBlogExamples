from delphifmx import *
from CurrencyConverter import Form2

def main():
    Application.Initialize()
    Application.Title = 'CurrencyConverter'
    Application.MainForm = Form2(Application)
    Application.MainForm.Show()
    Application.Run()
    Application.MainForm.Destroy()

if __name__ == '__main__':
    main()
