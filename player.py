import random
import logging

logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)
random.seed()


class Player:
    def __init__(self, name='Adventurer', gold=10, hp=10, armor_class=10):
        self.name = name
        self.armor_class = armor_class
        self.hp = hp
        self.gold = gold
        self.items = []  # anything that isnt a weapon/armor
        self.weapons = []
        self.armor = []

    def set_hp(self, hp):
        self.hp = hp

    def set_armor_class(self, new_armor_class):
        if new_armor_class < 0:
            logging.warning('AC was attempted to be set to a negative value!')
        else:
            self.armor_class = new_armor_class

    def display_attack_options(self):
        for i in range(len(self.weapons)):
            print(f'{i + 1}. {self.weapons[i]}')


class Warrior(Player):
    def __init__(self, name='Adventurer', hp=15, armor_class=10):
        super().__init__(name, hp, armor_class)
        self.weapons = ['Short Sword']
        self.armor = ['Chain Mail']

    def attack(self):
        # Generate a 'hit value'
        to_hit = random.randint(1, 20)
        attack_damage = random.randint(0, 6)
        return to_hit, attack_damage
