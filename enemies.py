class Enemy:
    def __init__(self, name='test', hp=5, armor_class=5):
        self.name = name
        self.display_char = '%'
        self.armor_class = armor_class
        self.hp = hp
        self.items = []  # anything that isnt a weapon/armor
        self.weapons = []
        self.armor = []

    def basic_attack(self):
        pass


class Goblin(Enemy):
    def __init__(self, name='Goblin', hp=10, armor_class=8):
        super().__init__(name, hp, armor_class)
        self.weapons.append('Wooden Sword') # testing purposes for now

    def basic_attack(self):
        pass

    def movement(self):