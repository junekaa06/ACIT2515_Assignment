from abstract_player import AbstractPlayer

class Center(AbstractPlayer):

    def __init__(self, player_id, first_name, last_name, height, weight, year_drafted, num_rebounds, play_type):
        super().__init__(player_id, first_name, last_name, height, weight, year_drafted)
        if num_rebounds < 0:
            raise ValueError("Number of rebounds should be positive")
        if type(play_type) != str:
            raise ValueError("Play-type should be a string")
        self._num_rebounds = num_rebounds
        self._play_type = play_type

    def get_description(self):
        details = ("%d: %s %s is %.2f cm tall, weighs %.2f kg, drafted on %d, has %d rebounds and plays %s") % (self._player_id, self._first_name, self._last_name, self._height, self._weight, self._year_drafted, self._num_rebounds, self._play_type)
        return details

    def get_num_rebounds(self):
        return self._num_rebounds

    def get_play_type(self):
        return self._play_type

    def get_type(self):
        return AbstractPlayer.CENTER_TYPE