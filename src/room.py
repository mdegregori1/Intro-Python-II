# Implement a class to hold room information. This should have name and
# description attributes.

# Fill out Player and Room classes in `player.py` and `room.py`

class Room():
    def __init__(self, name, description, item):
        self.name = name
        self.description = description
        self.item = item
        self.n_to = None
        self.e_to = None
        self.s_to = None
        self.w_to = None

    


# The room should also have `n_to`, `s_to`, `e_to`, and `w_to` attributes