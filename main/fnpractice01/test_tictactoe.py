from fn_tic_tac_toe import TicTacToe

tictactoe_game = TicTacToe()

tictactoe_game._draw_empty_board()

tictactoe_game.play_game()
# board_status=[["o","o","x"],["x","o","o"],["o","x","o"]]

# x_player="x_player"
# o_player="o_player"
# x_player_choice="x"
# o_player_choice="o"


# def is_winner(board_status):
    
#     is_full = False
#     row1=board_status[0]
#     row2=board_status[1]
#     row3=board_status[2]
#     winner_player="none"
    
#     if row1[0] == x_player_choice and row1[1] == x_player_choice and row1[2] == x_player_choice: 
#         print("row1 taken by x player ")
#         winner_player=x_player
#     elif row2[0] == x_player_choice and row2[1] == x_player_choice and row2[2] == x_player_choice: 
#         print("row2 taken by x player ")
#         winner_player=x_player
#     elif row3[0] == x_player_choice and row3[1] == x_player_choice and row3[2] == x_player_choice: 
#         print("row3 taken by x player ")
#         winner_player=x_player
    
#     elif row1[0] == x_player_choice and row2[0] == x_player_choice and row3[0] == x_player_choice: 
#         print("col1 taken by x player ")
#         winner_player=x_player
#     elif row1[1] == x_player_choice and row2[1] == x_player_choice and row3[1] == x_player_choice: 
#         print("col2 taken by x player ")
#         winner_player=x_player
#     elif row1[2] == x_player_choice and row2[2] == x_player_choice and row3[2] == x_player_choice: 
#         print("col3 taken by x player ")
#         winner_player=x_player
    
#     elif row1[0] == x_player_choice and row2[1] == x_player_choice and row3[2] == x_player_choice: 
#         print("diagnol topL->BottomR taken by x player ")
#         winner_player=x_player
#     elif row1[2] == x_player_choice and row2[1] == x_player_choice and row3[0] == x_player_choice: 
#         print("diagnol topR->BottomL taken by x player ")
#         winner_player=x_player
    
#     elif row1[0] == o_player_choice and row1[1] == o_player_choice and row1[2] == o_player_choice: 
#         print("row1 taken by o player ")
#         winner_player=o_player
        
#     elif row2[0] == o_player_choice and row2[1] == o_player_choice and row2[2] == o_player_choice: 
#          print("row2 taken by o player ")
#          winner_player=o_player
    
#     elif row3[0] == o_player_choice and row3[1] == o_player_choice and row3[2] == o_player_choice: 
#          print("row3 taken by o player ")
#          winner_player=o_player
    
#     elif row1[0] == o_player_choice and row2[0] == o_player_choice and row3[0] == o_player_choice: 
#         print("col1 taken by o player ")
#         winner_player=o_player
#     elif row1[1] == o_player_choice and row2[1] == o_player_choice and row3[1] == o_player_choice: 
#         print("col2 taken by o player ")
#         winner_player=o_player
#     elif row1[2] == o_player_choice and row2[2] == o_player_choice and row3[2] == o_player_choice: 
#         print("col3 taken by o player ")
#         winner_player=o_player
    
#     elif row1[0] == o_player_choice and row2[1] == o_player_choice and row3[2] == o_player_choice: 
#         print("diagnol topL->BottomR taken by o player ")
#         winner_player=o_player
#     elif row1[2] == o_player_choice and row2[1] == o_player_choice and row3[0] == o_player_choice: 
#         print("diagnol topR->BottomL taken by o player ")
#         winner_player=o_player
    
#     else: 
#          print("no one won----->")
#          winner_player="none"
#     return winner_player 


# print("find winner")
# is_winner(board_status)