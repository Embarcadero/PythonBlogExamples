from delphifmx import *
from Main import MainForm

def main():
    Application.MainForm = MainForm(Application)
    Application.MainForm.Show()

if __name__ == '__main__':
    main()
