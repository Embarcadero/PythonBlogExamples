import os
from delphifmx import *

class TicTacToeGUI(Form):

    def __init__(self, owner):
        self.Title = None
        self.Status = None
        self.Line1 = None
        self.Line2 = None
        self.Line3 = None
        self.Line4 = None
        self.Pos1 = None
        self.Pos2 = None
        self.Pos3 = None
        self.Pos4 = None
        self.Pos6 = None
        self.Pos5 = None
        self.Pos7 = None
        self.Pos8 = None
        self.Pos9 = None
        self.LoadProps(os.path.join(os.path.dirname(os.path.abspath(__file__)), "TicTacToe.pyfmx"))

        self.board = [[self.Pos1.Text, self.Pos2.Text, self.Pos3.Text], \
                    [self.Pos4.Text, self.Pos5.Text, self.Pos6.Text], \
                    [self.Pos7.Text, self.Pos8.Text, self.Pos9.Text]]
        self.p1 = "X"
        self.p2 = "O"
        self.player_status = 1

    def make_move(self, player, row, col, Pos):
        if Pos.Text != "":
            self.Status.Text = "Please try again!"
        else:
            self.board[row][col] = player
            Pos.Text = player
            if player == "X":
                self.player_status = 2
            else:
                self.player_status = 1

            if self.has_winner()==True:
                pass
            elif len("".join([self.board[i][j] for i in range(3) for j in range(3)])) == 9:
                self.Status.Text = "Tie! Game Over!"
            else:
                self.Status.Text = "Player "+ str(self.player_status) + " Move"

    def Pos1Click(self, Sender):
        if self.player_status == 1:
            self.make_move(self.p1, 0, 0, self.Pos1)
        else:
            self.make_move(self.p2, 0, 0, self.Pos1)

    def Pos2Click(self, Sender):
        if self.player_status == 1:
            self.make_move(self.p1, 0, 1, self.Pos2)
        else:
            self.make_move(self.p2, 0, 1, self.Pos2)

    def Pos3Click(self, Sender):
        if self.player_status == 1:
            self.make_move(self.p1, 0, 2, self.Pos3)
        else:
            self.make_move(self.p2, 0, 2, self.Pos3)

    def Pos4Click(self, Sender):
        if self.player_status == 1:
            self.make_move(self.p1, 1, 0, self.Pos4)
        else:
            self.make_move(self.p2, 1, 0, self.Pos4)

    def Pos5Click(self, Sender):
        if self.player_status == 1:
            self.make_move(self.p1, 1, 1, self.Pos5)
        else:
            self.make_move(self.p2, 1, 1, self.Pos5)

    def Pos6Click(self, Sender):
        if self.player_status == 1:
            self.make_move(self.p1, 1, 2, self.Pos6)
        else:
            self.make_move(self.p2, 1, 2, self.Pos6)

    def Pos7Click(self, Sender):
        if self.player_status == 1:
            self.make_move(self.p1, 2, 0, self.Pos7)
        else:
            self.make_move(self.p2, 2, 0, self.Pos7)

    def Pos8Click(self, Sender):
        if self.player_status == 1:
            self.make_move(self.p1, 2, 1, self.Pos8)
        else:
            self.make_move(self.p2, 2, 1, self.Pos8)

    def Pos9Click(self, Sender):
        if self.player_status == 1:
            self.make_move(self.p1, 2, 2, self.Pos9)
        else:
            self.make_move(self.p2, 2, 2, self.Pos9)

       

    def has_winner(self):
        winner = None
        for i in range(3):
            # Check row combos
            if self.board[i][0] != "" and self.board[i][0] == self.board[i][1] and self.board[i][1] == self.board[i][2]:
                winner = self.board[i][0]
               
            # Check column combos
            elif self.board[0][i] != "" and self.board[0][i] == self.board[1][i] and self.board[1][i] == self.board[2][i]:
                winner = self.board[0][i]

        # Check Diagonals
        if self.board[0][0] != "" and self.board[0][0] == self.board[1][1] and self.board[1][1] == self.board[2][2]:
            winner= self.board[0][0]
        elif self.board[0][2] != "" and self.board[0][2] == self.board[1][1] and self.board[1][1] == self.board[2][0]:
            winner = self.board[0][2]

        if winner != None:
            if winner == "X":
                self.Status.Text = "Player 1 Won the Match"
            else:
                self.Status.Text = "Player 2 Won the Match"

            return True

    def ResetClick(self, Sender):
        self.board = [["", "", ""], \
                    ["", "", ""], \
                    ["", "", ""]]
        self.p1 = "X"
        self.p2 = "O"
        self.player_status = 1

        self.Pos1.Text = ""
        self.Pos2.Text = ""
        self.Pos3.Text = ""
        self.Pos4.Text = ""
        self.Pos5.Text = ""
        self.Pos6.Text = ""
        self.Pos7.Text = ""
        self.Pos8.Text = ""
        self.Pos9.Text = ""

        self.Status.Text = "Player "+ str(self.player_status) + " Move"
