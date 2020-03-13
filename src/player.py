# Write a class to hold player information, e.g. what room they are in
# currently.

# Fill out Player and Room classes in `player.py` and `room.py`
class Player():
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.items = []
    def travel(self, direction):
        if direction == 'n' and self.current_room.n_to is not None:
            print("\nYou just moved north!\n")
            print("")
            self.current_room = self.current_room.n_to
        elif direction == 's' and self.current_room.s_to is not None:
            print("\nYou just moved south!\n")
            print("")
            self.current_room = self.current_room.s_to
        elif direction == 'w' and self.current_room.w_to is not None:
            print("\nYou just moved west!\n")
            print("")
            self.current_room = self.current_room.w_to
        elif direction == 'e' and self.current_room.e_to is not None:
            print("\nYou just moved east!\n")
            print("")
            self.current_room = self.current_room.e_to
        else: 
            print("You can't go that way")
