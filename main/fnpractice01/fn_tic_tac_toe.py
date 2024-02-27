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
    
    def __init__(self, size_of_board = 3):
        self.size_of_board=size_of_board
        self.empty_filler="   "
    
    def _draw_empty_board(self):
        print(f"{self.empty_filler}|{self.empty_filler}|{self.empty_filler}")
        print("---+---+---") # divider
        print(f"{self.empty_filler}|{self.empty_filler}|{self.empty_filler}")
        print("---+---+---") # divider
        print(f"{self.empty_filler}|{self.empty_filler}|{self.empty_filler}")
        
    def _draw_player_choice_selected_board(self):
        print(f"{self.empty_filler}|{self.empty_filler}|{self.empty_filler}")
        print("---+---+---") # divider
        print(f"{self.empty_filler}|{self.empty_filler}|{self.empty_filler}")
        print("---+---+---") # divider
        print(f"{self.empty_filler}|{self.empty_filler}|{self.empty_filler}")