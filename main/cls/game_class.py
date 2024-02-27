class Game:
    
    def __init__(self, gname, gplayers):
        self.gname=gname
        self.gplayers=gplayers
        self.__game_details ={"football": 18, "Hockey":11, "Cricket": 9}
        
    def howmany_player_in_game(self, gname):
        if gname in self.__game_details:
            return self.__game_details[gname]
        else:
            return "game is not defined"
    
    def __str__(self):
        obj_details = "Name of game:" + self.gname + "\nNumber of players :" + str(self.gplayers)
        return obj_details


