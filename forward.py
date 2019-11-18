from abstract_player import AbstractPlayer

class Forward(AbstractPlayer):

    def __init__(self, player_id, first_name, last_name, height, weight, year_drafted, player_type, num_shots_took, num_shots_made):
        super().__init__(player_id, first_name, last_name, height, weight, year_drafted,player_type)
        if num_shots_took < 0:
            raise ValueError("Number of shots took should be positive")
        if num_shots_made < 0:
            raise ValueError("Number of shots made should be positive")
        self._num_shots_took = num_shots_took
        self._num_shots_made = num_shots_made

    def get_description(self):
        """ Gets description of Forward """
        details = ("%d: %s %s is %.2f cm tall, weighs %.2f kg, drafted on %d, took %d shots and made %d") % (self._player_id, self._first_name, self._last_name, self._height, self._weight, self._year_drafted, self._num_shots_took, self._num_shots_made)
        return details

    def get_num_shots_took(self):
        """ Gets number of shots took """
        return self._num_shots_took

    def get_num_shots_made(self):
        """ Gets number of shots made """
        return self._num_shots_made
    
    def get_type(self):
        """ Gets player type """
        return AbstractPlayer.FORWARD_TYPE

    def to_dict(self):
        """ Returns a dictionary representation of a Forward """
        dict = {}
        dict['player_id'] = self._player_id
        dict['first_name'] = self._first_name
        dict['last_name'] = self._last_name
        dict['height'] = self._height
        dict['weight'] = self._weight
        dict['year_drafted'] = self._year_drafted
        dict['player_type'] = self._player_type
        dict['num_shots_took'] = self._num_shots_took
        dict['num_shots_made'] = self._num_shots_made
        return dict