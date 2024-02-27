from game_class import Game
from players_cls import Player

game1 = Game("ICEHockey",6)
print(game1)

g_name="football"
print(f"Players in game {g_name} using function :", game1.howmany_player_in_game(g_name))

g_name="football-2"
print(f"Players in game {g_name} using function :", game1.howmany_player_in_game(g_name))

Player.play("Football")