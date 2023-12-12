class Enemy:
    def __init__(self, name='Slime', hp=5, armor_class=5):
        self.name = name
        self.armor_class = armor_class
        self.hp = hp
        self.items = [] # anything that isnt a weapon/armor
        self.weapons = []
        self.armor = []