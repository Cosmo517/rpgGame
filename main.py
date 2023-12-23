from player import *
from dungeon import *
import keyboard



def print_classes():
    for i in range(len(classes)):
        print(f'{i + 1}. {classes[i]}')


# the different classes available
classes = ['Warrior', 'Ranger', 'Wizard']

# 3 different subclasses, use for later
subclasses = [['Thief', 'Knight'], [''], ['Priest', 'Necromancer']]

# print('Welcome! Please select your class by typing the class '
#       'name:')
#
# print_classes()
#
# user_class_selection = input('> ')
#
# while user_class_selection not in classes:
#     print('That class does not exist, please type the correct name '
#           'from the list below')
#     print_classes()
#     user_class_selection = input('> ')
#
# user_name = input('What is your characters name? ')
#
# if user_class_selection == 'Warrior':
#     player_character = Warrior(user_name)

player_character = Warrior("test")

test_maze = Dungeon(player_character, 15, 15, )
test_maze.square_room()
test_maze.insert_player(4, 4)
test_maze.print_map()

moves = ['w', 'a', 's', 'd']

# Simple game loop for capturing player input
while True:
    event = keyboard.read_event()
    if event.event_type == keyboard.KEY_DOWN:
        if event.name in moves:
            test_maze.handle_player_movement(event.name)
            test_maze.handle_enemy_actions()

        if event.name == 'f':
            test_maze.generate_enemy()

        # debug for dijkstra map
        if event.name == 'm':
            test_maze.print_map_to_player()



# testing for json stuff

# dictionary = {
#     "name": "sathiyajith",
#     "rollno": 56,
#     "cgpa": 8.6,
#     "phonenumber": "9976770500"
# }
#
# # Serializing json
# json_object = json.dumps(dictionary, indent=4)
#
# # Writing to sample.json
# with open("sample.json", "w") as outfile:
#     outfile.write(json_object)
