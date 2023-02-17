from delphifmx import *
from Calculator import Form2

def main():
    Application.MainForm = Form2(Application)
    Application.MainForm.Show()

if __name__ == '__main__':
    main()
