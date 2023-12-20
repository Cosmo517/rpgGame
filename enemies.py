class Enemy:
    def __init__(self, name='test', hp=5, armor_class=5):
        self.name = name
        self.display_char = '%'
        self.armor_class = armor_class
        self.hp = hp
        self.items = []  # anything that isnt a weapon/armor
        self.weapons = []
        self.armor = []
        self.movement_modifier = 1  # number of spaces to move during one turn

    def basic_attack(self):
        """Basic attack for an enemy"""
        pass

    def get_display_char(self):
        """Returns the display character for an enemy"""
        return self.display_char


class Goblin(Enemy):
    def __init__(self, name='Goblin', hp=10, armor_class=8):
        super().__init__(name, hp, armor_class)
        self.display_char = 'g'
        self.weapons.append('Wooden Sword')  # testing purposes for now

    def basic_attack(self):
        pass

    def movement(self):
        pass
