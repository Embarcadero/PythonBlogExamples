from delphifmx import *
from TicTacToe import TicTacToeGUI

def main():
    Application.Initialize()
    Application.Title = 'TicTacToe'
    Application.MainForm = TicTacToeGUI(Application)
    Application.MainForm.Show()
    Application.Run()

if __name__ == '__main__':
    main()