from delphifmx import *
from MainForm import Main


def main():
    Application.MainForm = Main(Application)
    Application.MainForm.Show()


if __name__ == '__main__':
    main()
