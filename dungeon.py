from enemies import *
import os
import logging
import random

import tiles
from tiles import *

logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)


class Dungeon:
    def __init__(self, player_character, width=10, height=10):
        self.maze_height = height  # height of the dungeon
        self.maze_width = width  # width of the dungeon
        self.player_character = player_character  # the player's character in the dungeon
        self.user_position_x = -1  # user position in the dungeon (x)
        self.user_position_y = -1  # user position in the dungeon (y)
        self.dungeon_map = [[Tile() for x in range(self.maze_width)] for y in range(self.maze_height)]  # tiles
        self.enemies = []  # a list of enemies in the dungeon and their location

    def square_room(self):
        """Create a simple square room, with height and width
        of the dungeon."""
        for i in range(self.maze_height):
            for j in range(self.maze_width):
                if i == 0 or i == self.maze_height - 1 or j == 0 or j == self.maze_width - 1:
                    self.dungeon_map[i][j].set_display_char('#')
                    self.dungeon_map[i][j].set_walkable(False)

    def random_sized_room(self):
        """A single random sized room is created, bounded from
        0 to the height (and width) of the dungeon."""
        width = random.randint(0, self.maze_height - 1)
        height = random.randint(0, self.maze_width - 1)
        for i in range(height):
            for j in range(width):
                if i == 0 or i == self.maze_height - 1 or j == 0 or j == self.maze_width - 1:
                    self.dungeon_map[i][j].set_display_char('#')
                    self.dungeon_map[i][j].set_walkable(False)

    def generate_enemy(self):
        """Handles generating a single enemy (goblin) within the dungeon"""
        while True:
            pos_x = random.randint(1, self.maze_width - 1)
            pos_y = random.randint(1, self.maze_height - 1)
            if not self.dungeon_map[pos_y][pos_x].has_entity() and not self.dungeon_map[pos_y][pos_x].is_wall():
                break
        enemy = Goblin()
        enemy_info = [enemy, pos_x, pos_y]
        self.enemies.append(enemy_info)
        self.dungeon_map[pos_y][pos_x].set_entity(enemy)
        self.dungeon_map[pos_y][pos_x].set_display_char(enemy.get_display_char())
        os.system('cls')
        self.print_map()


    # this is a poor implementation of placing the player
    # it can cause a player to be placed out of bounds if the room
    # size is smaller than the size of the actual maze
    def insert_player(self, x: int, y: int):
        """Insert the player into the dungeon in a tile specified
        by x, y. If the tile is a wall (or an invalid tile), it will return a logging
        error."""
        if x < 0 or x > (self.maze_width - 1) or (y < 0 or y > (self.maze_height - 1))\
                or self.dungeon_map[y][x] == '#':
            logging.warning(f'failed inserting user into maze... x = %d, y = %d', x, y)
        else:
            self.user_position_x = x
            self.user_position_y = y
            self.dungeon_map[y][x].set_display_char('@')
            self.dungeon_map[y][x].set_entity(self.player_character)

    def handle_player_movement(self, key_pressed: str):
        """Handle the movement of the player when they press a related key, wasd"""
        move_dict = {'w': (0, -1), 'a': (-1, 0), 's': (0, 1), 'd': (1, 0)}  # this is in x,y form
        new_x, new_y = 0, 0
        if key_pressed in move_dict:
            move_x, move_y = move_dict[key_pressed]
            new_x, new_y = self.user_position_x + move_x, self.user_position_y + move_y

        if (0 <= new_y < self.maze_height and 0 <= new_x < self.maze_width and
           not self.dungeon_map[new_y][new_x].is_wall() and self.dungeon_map[new_y][new_x].get_walkable()):
            self.dungeon_map[self.user_position_y][self.user_position_x].set_display_char(' ')
            self.dungeon_map[self.user_position_y][self.user_position_x].set_entity(None)
            self.user_position_y, self.user_position_x = new_y, new_x
            self.dungeon_map[self.user_position_y][self.user_position_x].set_display_char('@')
            self.dungeon_map[self.user_position_y][self.user_position_x].set_entity(self.player_character)
            os.system('cls')
            self.print_map()

        if key_pressed == 'f':
            self.generate_enemy()

    def handle_enemy_movement(self, enemy_info):
        """Handle the enemy movement given a list of enemy info"""
        enemy, pos_x, pos_y = enemy_info[0], enemy_info[1], enemy_info[2]
        move_dict = {'w': (0, -1), 'a': (-1, 0), 's': (0, 1), 'd': (1, 0)}
        attempts = 0
        while True and attempts < 50:
            move_x, move_y = random.choice(list(move_dict.values()))

            new_x = enemy.movement_modifier * move_x + pos_x
            new_y = enemy.movement_modifier * move_y + pos_y
            if not self.dungeon_map[new_y][new_x].has_entity() and not self.dungeon_map[new_y][new_x].is_wall():
                enemy_info[1] = new_x
                enemy_info[2] = new_y
                break
            attempts += 1

        if (0 <= new_y < self.maze_height and 0 <= new_x < self.maze_width and
           not self.dungeon_map[new_y][new_x].is_wall() and self.dungeon_map[new_y][new_x].get_walkable()):
            self.dungeon_map[pos_y][pos_x].set_display_char(' ')
            self.dungeon_map[pos_y][pos_x].set_entity(None)
            self.dungeon_map[new_y][new_x].set_display_char(enemy.get_display_char())
            self.dungeon_map[new_y][new_x].set_entity(enemy)

    def handle_enemy_actions(self):
        """Handle enemy actions, such as movement, attacks"""
        for i in range(len(self.enemies)):
            self.handle_enemy_movement(self.enemies[i])
        os.system('cls')
        self.print_map()
        print(self.enemies)

    def print_map(self):
        """Print the map of the dungeon"""
        for i in range(self.maze_height):
            s = ' '
            for j in range(self.maze_width):
                s += self.dungeon_map[i][j].get_display_char()
            print(s)



