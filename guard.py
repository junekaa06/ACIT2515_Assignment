from abstract_player import AbstractPlayer

class Guard(AbstractPlayer):

    def __init__(self, player_id, first_name, last_name, height, weight, year_drafted, player_type, num_steals, num_assists):
        super().__init__(player_id, first_name, last_name, height, weight, year_drafted, player_type)
        if num_steals < 0:
            raise ValueError("Number of steals made should be positive")
        if num_assists < 0:
            raise ValueError("Number of assists should be positive")
        self._num_steals = num_steals
        self._num_assists = num_assists

    def get_description(self):
        """ Returns a description of Guard """
        details = ("%d: %s %s is %.2f cm tall, weighs %.2f kg, drafted on %d, has %d steals and %d assists") % (self._player_id, self._first_name, self._last_name, self._height, self._weight, self._year_drafted, self._num_steals, self._num_assists)
        return details

    
    def get_num_assists(self):
        """ Returns number of assists """
        return self._num_assists

    def get_num_steals(self):
        """ Returns number of steals """
        return self._num_steals
    
    def get_type(self):
        """ Returns the type of AbstractPlayer """
        return AbstractPlayer.GUARD_TYPE

    def to_dict(self):
        """ Returns a dictionary representation of a Guard """
        dict = {}
        dict['player_id'] = self._player_id
        dict['first_name'] = self._first_name
        dict['last_name'] = self._last_name
        dict['height'] = self._height
        dict['weight'] = self._weight
        dict['year_drafted'] = self._year_drafted
        dict['player_type'] = self._player_type
        dict['num_steals'] = self._num_steals
        dict['num_assists'] = self._num_assists

        return dict