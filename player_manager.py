from abstract_player import AbstractPlayer
from player_stats import PlayerStats
from guard import Guard
from forward import Forward
from center import Center

#Player manager class
class PlayerManager:
    """ Array for team """
    _next_available_id = 1

    def __init__(self, team_name):
        self._team_name = team_name
        self._players = []

    #Adds a player to the list
    def add_player(self, player_object):
        for player in self._players:
            if player.get_player_id() == self._next_available_id:
                raise ValueError("Cannot add duplicate product!" + " " + str(player_object.get_player_id()) + " " + player_object.get_player_first_name())

        player_object.set_player_id(self._next_available_id)
        self._players.append(player_object)
        self._next_available_id = self._next_available_id + 1
    
    #Gets the team name
    def get_team_name(self):
        return self._team_name
    
    #gets specific player based on ID
    def get_player(self, player_id):
        for player in self._players:
            if player_id == player.get_player_id():
                return player
        return None

    #Gets all players
    def get_all(self):
        return self._players

    #Gets player statistics
    def get_players_stats(self):
        num_guards = 0
        num_forwards = 0
        num_centers = 0
        total_num_players = 0
        avg_years_played = 0
        for player in self._players:
            total_num_players = total_num_players + 1
            if type(player) == Guard:
                num_guards = num_guards + 1
            if type(player) == Forward:
                num_forwards = num_forwards + 1
            if type(player) == Center:
                num_centers = num_centers + 1
        player_stats = PlayerStats(total_num_players, num_guards, num_forwards, num_centers, avg_years_played)
        return player_stats

    #Gets all types of players and their info
    def get_all_by_type(self):
        description = ""
        description = description + "Guards: " + "\n"
        for player in self._players:
            if type(player) == Guard:
                player.__class__ = Guard
                description = description + "  " + player.get_description() + "\n"
        description = description + "Forwards: " + "\n"
        for player in self._players:
            if type(player) == Forward:
                player.__class__ = Forward
                description = description + "  " + player.get_description() + "\n"
        description = description + "Centers: " + "\n"
        for player in self._players:
            if type(player) == Center:
                player.__class__ = Center
                description = description + "  " + player.get_description() + "\n"
        return description

    #Deletes Player based on Player ID
    def delete_player(self, player_id):
        if type(player_id) is int:
            player = self.get_player(player_id)
            if player is not None:
                self._players.remove(player)
            else:
                return None
        else:
            return "Player ID should be an integer value"

    #Update Player based on Player object
    def update_player(self, update_player):
        for i in range(len(self._players)):
            if self._players[i].get_player_id() == update_player.get_player_id():
                self._players[i] = update_player
        


    @staticmethod
    def _validate_string_input(display_name, str_value):
        """ Private helper to validate string values """
        if str_value is None:
            raise ValueError(display_name + " cannot be undefined.")

        if str_value == "":
            raise ValueError(display_name + " cannot be empty.")

   
                
        
