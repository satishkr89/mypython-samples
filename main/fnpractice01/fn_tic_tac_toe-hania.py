import random

# -------------------------------
# Tic Tac Toe

# Task1: Make a board by using list of 9 indices having ' ' or '_' representing the 9 places in the Tic Tac Toe board. 
# You can make a 9x1 list or even a 3x3 nested list. Board will be a global variable accessible in all functions.
# The two players will be using 'x' and 'o'. 
# So you can use 'x' and 'o' to represent the players themselves.

# Task2: Write a function named toss() that has no parameter. 
# This function selects x or o randomly and returns the player who won the toss
# Using this function you are going to select the player to start from

# Task3: Show the board to the player. 
# You can use this template to begin with and then show the updated board every time using the list
#    |   |
# ---+---+---
#    |   | 
# ---+---+---
#    |   | 

# Task4: Ask the player to select the position where he wants to place 'x' or 'o'

# Task5: Write a function named check_board_position() that has one parameter of position.
# This function checks if the position the player has selected is empty or not and returns True or False.
# If the position is empty then proceed to Task6, 
# otherwise keep o asking again and again until the player enters a valid position

# Task6: Write a function named update_board() that has two paramters of position and player.
# This function puts 'x' or 'o' on the specific position depending upon whose turn was it. 

# Task7: Make a function named as check_if_won() that has no parameters.
# This function checks all the possibilites of a player to win.
# So you have to check all the possible winning combinations of a symbol. 
# If A player has won the game return True otherwise return False.

# Check if the player had won after placing its symbol on the board.
# Note that the first possibility of any one of the players to win is that it's the fifth overall turn in the game.
# Such as this board:
#  x | o |
# ---+---+---
#  o | x | 
# ---+---+---
#    |   | x

# Task8: If a player won the game then display if 'x' or 'o' won and end the game.

# Task9: If no one has won the game yet then switch the turn to the other player and continue again from Task3.
# For switching the turn: if the current player is 'x' the turn must switch to 'o' 
# and if the current player is 'o' the turn must switch to 'x' 

class TicTacToe:
    
    def __init__(self):
        self.board=[[" "," "," "],[" "," "," "],[" "," "," "]]
        self.players = ["x", "o"]
        self.turn = None
        
    def _draw_board(self):
        print("    \tCol1 | Col2 | Col3")
        print("    \t-----+------+-----") # divider
        for i in range(len(self.board)):
            print(f"Row{i+1}\t  {self.board[i][0]}  |   {self.board[i][1]}  |  {self.board[i][2]}")
            print("    \t-----+------+-----") # divider

    def toss(self):
        return random.choice(self.players)
    
    def is_valid_position(self, player_choice):
        if len(player_choice) == 4 and player_choice[1].isnumeric() and player_choice[3].isnumeric():
            row = int(player_choice[1])
            col = int(player_choice[3])
            if 1<=row<=3 and 1<=col<=3:
                if self.board[row-1][col-1] == " ":
                    return True
        
        print("Invalid choice")
        return False
    
    def get_position(self):
        while True:
            player_choice = input("Please enter row col : ")
            if player_choice == "q":
                return 'q'
        
            if self.is_valid_position(player_choice):
                row = int(player_choice[1])-1
                col = int(player_choice[3])-1
                return (row, col)


    def is_board_full(self):
        '''
        # direct way
        if (" " not in self.board[0] and " " not in self.board[1] and " " not in self.board[1]):
            return True
        else:
            return False
        '''
        # alternate way
        for row in self.board:
            if " " in row:
                return False
        return True
    
    # 00 01 02 
    # 10 11 12
    # 20 21 22
    def is_winner(self):
        # horizontal checks
        if (self.board[0][0] == self.turn and self.board[0][1] == self.turn and self.board[0][2] == self.turn):
            print(f"row1 is taken by Player {self.turn}")
            return True
        elif (self.board[1][0] == self.turn and self.board[1][1] == self.turn and self.board[1][2] == self.turn):
            print(f"row2 is taken by Player {self.turn}")
            return True
        elif (self.board[2][0] == self.turn and self.board[2][1] == self.turn and self.board[2][2] == self.turn):
            print(f"row3 is taken by Player {self.turn}")
            return True
        # vertical checks
        if (self.board[0][0] == self.turn and self.board[1][0] == self.turn and self.board[2][0] == self.turn):
            print(f"col1 is taken by Player {self.turn}")
            return True
        elif (self.board[0][1] == self.turn and self.board[1][1] == self.turn and self.board[2][1] == self.turn):
            print(f"col2 is taken by Player {self.turn}")
            return True
        elif (self.board[0][2] == self.turn and self.board[1][2] == self.turn and self.board[2][2] == self.turn):
            print(f"col3 is taken by Player {self.turn}")
            return True
        # diagonal checks
        if (self.board[0][0] == self.turn and self.board[1][1] == self.turn and self.board[2][2] == self.turn):
            print(f"diagnol topL->BottomR is taken by Player {self.turn}")
            return True
        elif (self.board[0][2] == self.turn and self.board[1][1] == self.turn and self.board[2][0] == self.turn):
            print(f"diagnol topR->BottomL is taken by Player {self.turn}")
            return True
        elif self.is_board_full():
            print("no one won----->")
            return "Draw" 
        else:
            return False

    def update_board(self, row, col):
        self.board[row][col] = self.turn        

    
    def play_game(self):
        print("====================================================================")
        print("           Welcome to Tic Tac Toe Game")
        print("=====================================================================")
        print("      Rules: Make choice for empty cells")
        print("      How to make choice? select row number and column number")
        print("      for example r1c1 or r2c3. rows and columns can't be more than 3")
        print("      enter q for quitting")
        print("=====================================================================")
        
        self.turn = self.toss()
        print(f"\n Tossed ... winner of toss is : Player {self.turn}")
        if self.turn == "x":
            second_player = "o"
        else:
            second_player = "x"
        print(f"\n First player to make choice is : Player {self.turn}")    
        print(f"\n Second player to make choice is : Player {second_player}")  

        while(True):
            self._draw_board()

            print(f"Player {self.turn} Please make your choice: ")
                
            player_choice = self.get_position()
                    
            if player_choice == "q":
                print("Quitting game, player selected to quit")
                break
            else:
                row = player_choice[0]
                col = player_choice[1]
                self.update_board(row, col)

            winner_player = self.is_winner()
            if winner_player == "Draw":
                break
            elif winner_player == True:
                self._draw_board()
                print(f"Quitting game, the winning player is: Player {self.turn}")
                break

            if self.turn == "x":
                self.turn = "o"
            else:
                self.turn = "x"
                
            if self.is_board_full():
                print("Quitting game, board is full")
                break