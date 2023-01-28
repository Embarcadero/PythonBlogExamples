from delphifmx import *
from Calculator import Form2

def main():
    Application.Initialize()
    Application.Title = 'Calculator'
    Application.MainForm = Form2(Application)
    Application.MainForm.Show()
    Application.Run()
    Application.MainForm.Destroy()

if __name__ == '__main__':
    main()
