# the different classes available
classes = ['Warrior', 'Ranger', 'Wizard']

# 3 different subclasses, use for later
subclasses = [['Thief', 'Knight'], [''], ['Priest', 'Necromancer']]

print('Welcome! Please select your class:')

for i in range(len(classes)):
    print(f'{i + 1}. {classes[i]}')