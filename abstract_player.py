class AbstractPlayer:
    CENTER_TYPE = "CENTER"
    GUARD_TYPE = "GUARD"
    FORWARD_TYPE = "FORWARD"

    """ Representation of a Player on a basketball team """
    def __init__(self, player_id, first_name, last_name, height, weight, year_drafted):
        
        if type(player_id) != int:
            raise ValueError("Player number should be an integer value")
        self._player_id = player_id
        self._first_name = first_name
        self._last_name = last_name 
        self._height = height
        self._weight = weight
        self._year_drafted = year_drafted

    def get_description(self):
        """ Returns player details """
        details = "Number %d: %s %s is %.2f cm tall and weighs %.2f kg and was drafted on %s" % (self._player_id, self._first_name, self._last_name, self._height, self._weight, self._year_drafted)
        return details

    def set_player_id(self, player_id):
        """ Sets a player_id for a AbstractPlayer """
        self._player_id = player_id

    def get_player_id(self):
        """ Returns player_id """
        return self._player_id
    
    def get_player_first_name(self):
        """ Returns player's first name """
        return self._first_name

    def get_player_last_name(self):
        """ Returns player's last name """
        return self._last_name

    def get_player_height(self):
        """ Returns player's height """
        return self._height

    def get_player_weight(self):
        """ Returns player's weight """
        return self._weight
    
    def get_player_year_drafted(self):
        """ Returns player's year drafted """
        return self._year_drafted