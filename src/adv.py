from room import Room
from player import Player
from item import Item
import time 

# add items
items = [
    Item('Sword', 'A weapon used to abolish your enemies!'),
    Item('Health Potion', 'Hurt? Fear not. Drink this, and heal.'),
    Item('Armor', 'This bronze-cast armor will protect your health in battle.'),
    Item('High Damage Fuel', 'Drinking fuel increases the damage that you can do.'),
    Item('5 gold coins', 'Use gold coins to buy supplies!')
]
# package random import 
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", items[0]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", items[1]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", items[2]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", items[3]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", items[4]),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']



#
# Main
#

print("Hello player, what is your name?")
time.sleep(0.5)

# Make a new player object that is currently in the 'outside' room.
# should be input, though
player = Player(input('Please enter your name:'), room['outside'])
time.sleep(0.5)


print(f'Thank you, {player.name}! Ready to get started?')
time.sleep(0.5)

response = input('y or n')

if response == 'y':
    pass
elif response == 'n':
    print("Please come back when you're ready to play!")
    exit()
else:
    print("Sorry, I didn't recognize that command. Please try again.")
    exit()



# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

while True:
    player_name = player.current_room.name
    player_item = player.current_room.item
    room_description = player.current_room.description

    print(f"you are currently in '{player_name}'. We can see {player_item}")
    print('')
    print('description:',room_description)
    command = input("Enter 'w' to move west, 'n' to move north, 'e' to move east, or 's' to move south. To pick up an item, type 'take'. To drop it, type 'drop'. To quit, press 'q'. ")

    if command == 'w':
        if player.current_room.w_to:
            player.current_room = player.current_room.w_to
            print("You moved west!")
        else:
            print('You cannot move west!')
    elif command == 'n':
        if player.current_room.n_to:
            player.current_room = player.current_room.n_to
            print("You moved north!")
        else:
            print('You cannot move north!')
    elif command == 'e':
        if player.current_room.e_to:
            player.current_room = player.current_room.e_to
            print("You moved east!")
        else:
            print('You cannot move east!')
    elif command == 's':
        if player.current_room.s_to:
            player.current_room = player.current_room.s_to
            print("You moved south!")
        else:
            print('You cannot move south!')
    elif command == 'take':
        player.items.append(player.current_room.item.name)
        player_item = None 
        print('current items list:', player.items )
    elif command == 'drop':
        player.items.pop()
        print('current items list:', player.items)
    elif command == 'q':
        print('See you next time!')
        break
    else:
        print("Hm.. I didn't recognize that command. Please try again")