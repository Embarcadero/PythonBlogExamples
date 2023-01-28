from delphifmx import *
from TicTacToe import Form2

def main():
    Application.Initialize()
    Application.Title = 'TicTacToe'
    Application.MainForm = Form2(Application)
    Application.MainForm.Show()
    Application.Run()

if __name__ == '__main__':
    main()