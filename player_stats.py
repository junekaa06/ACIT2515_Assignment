class PlayerStats:
    """ Statistics on a basketball team """

    def __init__ (self, total_num_players, num_guards, num_forwards, num_centers, avg_years_played):

        if type(total_num_players) is None or type(total_num_players) != int:
            raise ValueError("Invalid value for total number of players")
        self._total_num_players = total_num_players
        if type(num_guards) is None or type(num_guards) != int:
            raise ValueError("Invalid value for total number of guards")
        self._num_guards = num_guards
        if type(num_forwards) is None or type(num_forwards) != int:
            raise ValueError("Invalid value for total number of forwards")
        self._num_forwards = num_forwards
        if type(num_centers) is None or type(num_centers) != int:
            raise ValueError("Invalid value for total number of centers")
        self._num_centers = num_centers
        if type(avg_years_played) is None or type(avg_years_played) != int:
            raise ValueError("Invalid value for average years played")
        self._avg_years_played = avg_years_played

    def get_total_num_players(self):
        """ Returns the number of total players """
        return self._total_num_players

    def get_num_guards(self):
        """ Returns the number of guards """
        return self._num_guards
    
    def get_num_forwards(self):
        """ Returns the number of forwards """
        return self._num_forwards

    def get_num_centers(self):
        """ Returns the number of centers """
        return self._num_centers
    
    def get_avg_years_played(self):
        """ Returns the average years played """
        return self._avg_years_played

    def to_dict(self):
        """ Returns a dictionary representation of a player """
        dict = {}
        dict['total_num_players'] = self._total_num_players
        dict['num_guards'] = self._num_guards
        dict['num_forwards'] = self._num_forwards
        dict['num_centers'] = self._num_centers
        dict['avg_years_played'] = self._avg_years_played

        return dict