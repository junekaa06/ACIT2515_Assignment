from abstract_player import AbstractPlayer
from player_stats import PlayerStats
from guard import Guard
from forward import Forward
from center import Center
import json
import os.path

#Player manager class
class PlayerManager:
    """ Array for team """
    _filepath = None

    def __init__(self, team_name, filepath):
        self._team_name = team_name
        self._players = []
        self._filepath = filepath
        self._read_players_from_file()

    def add_player(self, player_object):
        """ Adds a player to the list """
        self._players.append(player_object)
        self._write_players_to_file()
    
    def get_team_name(self):
        """ Gets the team name """
        return self._team_name
    
    def get_player(self, player_id):
        """ Gets specific player based on ID """
        for player in self._players:
            if player_id == player.get_player_id():
                return player
        return None

    def get_all(self):
        """ Gets all players """
        return self._players

    def get_players_stats(self):
        """ Gets player statistics """
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

    """ 
    
    OLD GET ALL BY TYPE
    
    
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
"""

    def get_all_by_type(self, type):
        """Gets all players by type"""

        players = []

        for player in self._players:
            if player.get_player_type() == type:
                players.append(player)
        return players
    
    def delete_player(self, player_id):
        """ Deletes Player based on Player ID """
        if type(player_id) is int:
            player = self.get_player(player_id)
            if player is not None:
                self._players.remove(player)
                self._write_players_to_file()
            else:
                raise ValueError("Player is not existent") 
        else:
            return "Player ID should be an integer value"

    def update_player(self, update_player):
        """ Update Player based on Player object """
        for i in range(len(self._players)):
            if self._players[i].get_player_id() == update_player.get_player_id():
                self._players[i] = update_player
                self._write_players_to_file()

    
    def _read_players_from_file(self):
        """ Reads players from file """
        with open(self._filepath, 'r') as input_file:
            players = json.load(input_file)
            for json_data in players:
                type = json_data["player_type"]
                if type == "center":
                    player_id = json_data["player_id"]
                    first_name = json_data["first_name"]
                    last_name = json_data["last_name"]
                    height = json_data["height"]
                    weight = json_data["weight"]
                    year_drafted = json_data["year_drafted"]
                    player_type = json_data["player_type"]
                    num_rebounds = json_data["num_rebounds"]
                    play_type = json_data["play_type"]
                    player = Center(player_id, first_name, last_name, height, weight, year_drafted, player_type, num_rebounds, play_type)
                elif type == "forward":
                    player_id = json_data["player_id"]
                    first_name = json_data["first_name"]
                    last_name = json_data["last_name"]
                    height = json_data["height"]
                    weight = json_data["weight"]
                    year_drafted = json_data["year_drafted"]
                    player_type = json_data["player_type"]
                    num_shots_took = json_data["num_shots_took"]
                    num_shots_made = json_data["num_shots_made"]
                    player = Forward(player_id, first_name, last_name, height, weight, year_drafted, player_type, num_shots_took, num_shots_made)
                elif type == "guard":
                    player_id = json_data["player_id"]
                    first_name = json_data["first_name"]
                    last_name = json_data["last_name"]
                    height = json_data["height"]
                    weight = json_data["weight"]
                    year_drafted = json_data["year_drafted"]
                    player_type = json_data["player_type"]
                    num_steals = json_data["num_steals"]
                    num_assists = json_data["num_assists"]
                    player = Guard(player_id, first_name, last_name, height, weight, year_drafted, player_type, num_steals, num_assists)
                self._players.append(player)
            return self._players
                

    def _write_players_to_file(self):
        """ Writes players to file """
        data = []
        for players in self._players:
            json_data = players.to_dict()
            data.append(json_data)
        with open(self._filepath, 'w+') as output_file:
            json.dump(data, output_file)
        


    @staticmethod
    def _validate_string_input(display_name, str_value):
        """ Private helper to validate string values """
        if str_value is None:
            raise ValueError(display_name + " cannot be undefined.")

        if str_value == "":
            raise ValueError(display_name + " cannot be empty.")

   
                
        
