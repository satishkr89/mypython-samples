import math
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
    x_player="x_player"
    o_player="o_player"
    x_player_choice="x"
    o_player_choice="o"
    board_status=[[" "," "," "],[" "," "," "],[" "," "," "]]
    possible_choices=[["r1c1","r1c2","r1c3"],["r2c1","r2c2","r2c3"],["r3c1","r3c2","r3c3"]]
    
    first_player_to_make_choice="none"
    second_player_to_make_choice="none"
    
    
    def __init__(self, size_of_board = 3):
        self.size_of_board=size_of_board
        self.empty_filler="   "
        # test line self.board_status=[["11","12","13"],["21","22","23"],["31","32","33"]]
        self.board_status=[[" "," "," "],[" "," "," "],[" "," "," "]]
        self.first_player_to_make_choice="none"
        self.second_player_to_make_choice="none"
    
    def _draw_empty_board(self):
        
        print("\n      ->   Col1|Col2|Col3\n")
        
        print(f"Row 1 -> {self.empty_filler}   |{self.empty_filler} |{self.empty_filler}")
        print("--------    ---+----+---") # divider
        print(f"Row 2 -> {self.empty_filler}   |{self.empty_filler} |{self.empty_filler}")
        print("--------    ---+----+---") # divider
        print(f"Row 3 -> {self.empty_filler}   |{self.empty_filler} |{self.empty_filler}\n")
        
    def _draw_player_choice_selected_board(self, board_status):
        i=1
        print("\n          Col1 | Col2 | Col3")
        print("------    -----+------+-----") # divider
        for row in self.board_status:
            print(f"Row {i}      {row[0]}   |  {row[1]}   | {row[2]}")
            i += 1
            print("------    -----+------+-----") # divider
    
    def toss(self):
        players = ["x_player", "o_player"]
        random.shuffle(players)
        toss_num = round(random.random()*100)
        if toss_num > 50:
            return players[0]
        else:
            return players[1]
    
        
    def is_board_full(self):
        is_full = False
        for row in self.board_status:
            if row[0] == self.x_player_choice or row[0] == self.o_player_choice: 
                if row[1] == self.x_player_choice or row[1] == self.o_player_choice: 
                    if row[2] == self.x_player_choice or row[2] == self.o_player_choice: 
                        is_full = True
                    else:
                        is_full = False
                        break
                else:
                    is_full = False
                    break
            else:
                is_full = False
                break
        return is_full 
    
    #following is not used
    def is_board_full_V1(self):
        is_full = False
        row1=self.board_status[0]
        row2=self.board_status[1]
        row3=self.board_status[2]
        if row1[0] == self.x_player_choice or row1[0] == self.o_player_choice: 
            is_full = True
        if row3[1] == self.x_player_choice or row3[1] == self.o_player_choice: 
            is_full = True
        if row2[2] == self.x_player_choice or row2[2] == self.o_player_choice: 
            is_full = True
        else:
            is_full= True
        return is_full 
    
    # try more efficient method to find winner
    def is_winnerv2(self):
        winner_player="none"
        for row in self.board_status:
            for col in row:
                if col  == self.x_player_choice:
                    print("row1 taken by x player ")
                elif col  == self.o_player_choice:
                    print("row1 taken by o player ")
    
    def is_winner(self):
        row1=self.board_status[0]
        row2=self.board_status[1]
        row3=self.board_status[2]
        winner_player="none"
        
        if row1[0] == self.x_player_choice and row1[1] == self.x_player_choice and row1[2] == self.x_player_choice: 
            print("row1 taken by x player ")
            winner_player=self.x_player
        elif row2[0] == self.x_player_choice and row2[1] == self.x_player_choice and row2[2] == self.x_player_choice: 
            print("row2 taken by x player ")
            winner_player=self.x_player
        elif row3[0] == self.x_player_choice and row3[1] == self.x_player_choice and row3[2] == self.x_player_choice: 
            print("row3 taken by x player ")
            winner_player=self.x_player
        elif row1[0] == self.x_player_choice and row2[0] == self.x_player_choice and row3[0] == self.x_player_choice: 
            print("col1 taken by x player ")
            winner_player=self.x_player
        elif row1[1] == self.x_player_choice and row2[1] == self.x_player_choice and row3[1] == self.x_player_choice: 
            print("col2 taken by x player ")
            winner_player=self.x_player
        elif row1[2] == self.x_player_choice and row2[2] == self.x_player_choice and row3[2] == self.x_player_choice: 
            print("col3 taken by x player ")
            winner_player=self.x_player
        elif row1[0] == self.x_player_choice and row2[1] == self.x_player_choice and row3[2] == self.x_player_choice: 
            print("diagnol topL->BottomR taken by x player ")
            winner_player=self.x_player
        elif row1[2] == self.x_player_choice and row2[1] == self.x_player_choice and row3[0] == self.x_player_choice: 
            print("diagnol topR->BottomL taken by x player ")
            winner_player=self._player
        elif row1[0] == self.o_player_choice and row1[1] == self.o_player_choice and row1[2] == self.o_player_choice: 
            print("row1 taken by o player ")
            winner_player=self.o_player  
        elif row2[0] == self.o_player_choice and row2[1] == self.o_player_choice and row2[2] == self.o_player_choice: 
            print("row2 taken by o player ")
            winner_player=self.o_player
        elif row3[0] == self.o_player_choice and row3[1] == self.o_player_choice and row3[2] == self.o_player_choice: 
            print("row3 taken by o player ")
            winner_player=self.o_player
        elif row1[0] == self.o_player_choice and row2[0] == self.o_player_choice and row3[0] == self.o_player_choice: 
            print("col1 taken by o player ")
            winner_player=self.o_player
        elif row1[1] == self.o_player_choice and row2[1] == self.o_player_choice and row3[1] == self.o_player_choice: 
            print("col2 taken by o player ")
            winner_player=self.o_player
        elif row1[2] == self.o_player_choice and row2[2] == self.o_player_choice and row3[2] == self.o_player_choice: 
            print("col3 taken by o player ")
            winner_player=self.o_player
        elif row1[0] == self.o_player_choice and row2[1] == self.o_player_choice and row3[2] == self.o_player_choice: 
            print("diagnol topL->BottomR taken by o player ")
            winner_player=self.o_player
        elif row1[2] == self.o_player_choice and row2[1] == self.o_player_choice and row3[0] == self.o_player_choice: 
            print("diagnol topR->BottomL taken by o player ")
            winner_player=self.o_player
        else: 
            print("no one won----->")
            winner_player="none"
        return winner_player 
    
    def update_board(self, current_player, choice):
        #print(f"Board status is: {self.board_status}"
        if choice == "r1c1":
            row1 = self.board_status[0]
            col1 = row1[0]
            print(f" Row 1: {row1} Column 1 : {col1}")
            if col1 ==" " and current_player == self.o_player:
                row1[0] = self.o_player_choice
            elif col1 == self.o_player_choice and current_player == self.o_player:
                print("Invalid choice! Already selected.")
            elif col1 ==" " and current_player==self.x_player:
                row1[0] = self.x_player_choice
            elif col1 == self.x_player_choice and current_player==self.x_player:
                print("Invalid choice! Already selected.")
            else:
                print("Invalid choice! it shouldn't come to this section!")
        elif choice == "r1c2":
            row1 = self.board_status[0]
            col2 = row1[1]
            print(f" Row 1 Column 2 value is: {col2}")
            if col2 ==" " and current_player == self.o_player:
                row1[1] = self.o_player_choice
            elif col2 == self.o_player_choice and current_player == self.o_player:
                print("Invalid choice! Already selected.")
            elif col2 ==" " and current_player==self.x_player:
                row1[1] = self.x_player_choice
            elif col2 == self.x_player_choice and current_player==self.x_player:
                print("Invalid choice! Already selected.")
            else:
                print("Invalid choice! it shouldn't come to this section!")
            
        elif choice == "r1c3":
            row1 = self.board_status[0]
            col3 = row1[2]
            print(f" Row 1 Column 3 value is: {col3}")
            
            if col3 ==" " and current_player == self.o_player:
                row1[2] = self.o_player_choice
            elif col3 == self.o_player_choice and current_player == self.o_player:
                print("Invalid choice! Already selected.")
            elif col3 ==" " and current_player==self.x_player:
                row1[2] = self.x_player_choice
            elif col3 == self.x_player_choice and current_player==self.x_player:
                print("Invalid choice! Already selected.")
            
            else:
                print("Invalid choice! it shouldn't come to this section!")
        
        elif choice == "r2c1":
            row2 = self.board_status[1]
            col1 = row2[0]
            print(f" Row 2 Column 1 value is: {col1}")
            if col1 ==" " and current_player == self.o_player:
                row2[0] = self.o_player_choice
            elif col1 == self.o_player_choice and current_player == self.o_player:
                print("Invalid choice! Already selected.")
            elif col1 ==" " and current_player==self.x_player:
                row2[0] = self.x_player_choice
            elif col1 == self.x_player_choice and current_player==self.x_player:
                print("Invalid choice! Already selected.")
            else:
                print("Invalid choice! it shouldn't come to this section!")
            
            
            
        elif choice == "r2c2":
            row2 = self.board_status[1]
            col2 = row2[1]
            print(f" Row 2 Column 2 value is: {col2}")
            
            if col2 ==" " and current_player == self.o_player:
                row2[1] = self.o_player_choice
            elif col2 == self.o_player_choice and current_player == self.o_player:
                print("Invalid choice! Already selected.")
            elif col2 ==" " and current_player==self.x_player:
                row2[1] = self.x_player_choice
            elif col2 == self.x_player_choice and current_player==self.x_player:
                print("Invalid choice! Already selected.")
            else:
                print("Invalid choice! it shouldn't come to this section!")
            
            
        elif choice == "r2c3":
            row2 = self.board_status[1]
            col3 = row2[2]
            print(f" Row 2 Column 3 value is: {col3}")
            
            if col3 ==" " and current_player == self.o_player:
                row2[2] = self.o_player_choice
            elif col3 == self.o_player_choice and current_player == self.o_player:
                print("Invalid choice! Already selected.")
            elif col3 ==" " and current_player==self.x_player:
                row2[2] = self.x_player_choice
            elif col3 == self.x_player_choice and current_player==self.x_player:
                print("Invalid choice! Already selected.")
            else:
                print("Invalid choice! it shouldn't come to this section!")
        
        elif choice == "r3c1":
            row3 = self.board_status[2]
            col1 = row3[0]
            print(f" Row 3 Column 1 value is: {col1}")
            
            if col1 ==" " and current_player == self.o_player:
                row3[0] = self.o_player_choice
            elif col1 == self.o_player_choice and current_player == self.o_player:
                print("Invalid choice! Already selected.")
            elif col1 ==" " and current_player==self.x_player:
                row3[0] = self.x_player_choice
            elif col1 == self.x_player_choice and current_player==self.x_player:
                print("Invalid choice! Already selected.")
            else:
                print("Invalid choice! it shouldn't come to this section!")
            
        elif choice == "r3c2":
            row3 = self.board_status[2]
            col2 = row3[1]
            print(f" Row 3 Column 2 value is: {col2}")
            
            if col2 ==" " and current_player == self.o_player:
                row3[1] = self.o_player_choice
            elif col2 == self.o_player_choice and current_player == self.o_player:
                print("Invalid choice! Already selected.")
            elif col2 ==" " and current_player==self.x_player:
                row3[1] = self.x_player_choice
            elif col2 == self.x_player_choice and current_player==self.x_player:
                print("Invalid choice! Already selected.")
            else:
                print("Invalid choice! it shouldn't come to this section!")
            
        elif choice == "r3c3":
            row3 = self.board_status[2]
            col3 = row3[2]
            print(f" Row 3 Column 3 value is: {col3}")
            
            if col3 ==" " and current_player == self.o_player:
                row3[2] = self.o_player_choice
            elif col3 == self.o_player_choice and current_player == self.o_player:
                print("Invalid choice! Already selected.")
            elif col3 ==" " and current_player==self.x_player:
                row3[2] = self.x_player_choice
            elif col3 == self.x_player_choice and current_player==self.x_player:
                print("Invalid choice! Already selected.")
            else:
                print("Invalid choice! it shouldn't come to this section!")
            
        else:
            print(f"invalid choice: {choice}")
        

    
    def play_game(self):
        print("====================================================================")
        print("           Welcome to Tic Tac Toe Game")
        print("=====================================================================")
        print("      Rules: Make choice for empty cells")
        print("      How to make choice? select row number and column number")
        print("      for example r1c1 or r2c3. rows and columns can't be more than 3")
        print("      enter q for quitting")
        print("=====================================================================")
        
        self.first_player_to_make_choice=self.toss()
        print(f"\n Tossed ... winner of toss is : {self.first_player_to_make_choice}")
        if self.first_player_to_make_choice.startswith("o"):
            self.second_player_to_make_choice = "x_player"
        else:
            self.second_player_to_make_choice = "o_player"
        print(f"\n First player to make choice is : {self.first_player_to_make_choice}")    
        print(f"\n Second player to make choice is : {self.second_player_to_make_choice}")  

        try:
            self._draw_empty_board()
            current_player = self.first_player_to_make_choice
            while(True):
                print(f"{current_player} Please make your choice: ")
                player_choice = input("Please enter row col : ")
                if player_choice == "q":
                    print("Quitting game, player selected to quit")
                    break
                elif self.is_board_full():
                    print("Quitting game, board is full")
                    break
                else:
                    self.update_board(current_player, player_choice)
                    winner_player = self.is_winner()
                    if winner_player == "none":
                        pass
                    else:
                        print(f"Quitting game, the winning player is: {winner_player}")
                        break
                if current_player == self.first_player_to_make_choice:
                    current_player = self.second_player_to_make_choice
                else:
                    current_player = self.first_player_to_make_choice
                self.update_board(current_player, player_choice)
                self._draw_player_choice_selected_board(self.board_status)
            self._draw_player_choice_selected_board(self.board_status)       
        except Exception as exp:
            print("Exception....->", type(exp), exp )
            print("Exception....")