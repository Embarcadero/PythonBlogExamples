from delphifmx import *
from TicTacToe import TicTacToeGUI

def main():
    Application.MainForm = TicTacToeGUI(Application)
    Application.MainForm.Show()

if __name__ == '__main__':
    main()