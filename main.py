from player import *
import json

def print_classes():
    for i in range(len(classes)):
        print(f'{i + 1}. {classes[i]}')



# the different classes available
classes = ['Warrior', 'Ranger', 'Wizard']

# 3 different subclasses, use for later
subclasses = [['Thief', 'Knight'], [''], ['Priest', 'Necromancer']]

print('Welcome! Please select your class by typing the class '
      'name:')

print_classes()

user_class_selection = input('> ')

while user_class_selection not in classes:
    print('That class does not exist, please type the correct name '
          'from the list below')
    print_classes()
    user_class_selection = input('> ')

user_name = input('What is your characters name? ')

if user_class_selection == 'Warrior':
    player_character = Warrior(user_name)

user_attack_selection = 0


# on hold...

# create simple game loop for attacking

# while user_attack_selection != 4:
#     print('Please select an attack option by typing'
#           'in the number next to the attack')
#     player_character.display_attack_options()
#     user_attack_selection = input('> ')
#     if user_attack_selection == 4:
#         break
#
#     user_attack = player_character.attack()
#     print(user_attack)








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
