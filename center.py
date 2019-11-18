from abstract_player import AbstractPlayer

class Center(AbstractPlayer):

    def __init__(self, player_id, first_name, last_name, height, weight, year_drafted, player_type, num_rebounds, play_type):
        super().__init__(player_id, first_name, last_name, height, weight, year_drafted, player_type)
        if num_rebounds < 0:
            raise ValueError("Number of rebounds should be positive")
        if type(play_type) != str:
            raise ValueError("Play-type should be a string")
        self._num_rebounds = num_rebounds
        self._play_type = play_type

    def get_description(self):
        """ Gets description of Center """
        details = ("%d: %s %s is %.2f cm tall, weighs %.2f kg, drafted on %d, has %d rebounds and plays %s") % (self._player_id, self._first_name, self._last_name, self._height, self._weight, self._year_drafted, self._num_rebounds, self._play_type)
        return details

    def get_num_rebounds(self):
        """ Gets number of rebounds """
        return self._num_rebounds

    def get_play_type(self):
        """ Gets play type """
        return self._play_type

    def get_type(self):
        """ Gets player type """
        return AbstractPlayer.CENTER_TYPE

    def to_dict(self):
        """ Returns a dictionary representation of a Center """
        dict = {}
        dict['player_id'] = self._player_id
        dict['first_name'] = self._first_name
        dict['last_name'] = self._last_name
        dict['height'] = self._height
        dict['weight'] = self._weight
        dict['year_drafted'] = self._year_drafted
        dict['player_type'] = self._player_type
        dict['num_rebounds'] = self._num_rebounds
        dict['play_type'] = self._play_type

        return dict
