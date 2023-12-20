class Tile:
    """
    Defines what a tile is, as well as its methods.
    """
    def __init__(self, display_char=' ', item=None, entity=None):
        self.display_char = display_char
        self.item = item
        self.entity = entity
        self.walkable = True

    def is_wall(self):
        """Checks if the tile is a wall or not"""
        if not self.walkable and self.display_char == '#':
            return True
        else:
            return False

    def has_entity(self):
        """Checks if the current tile has an entity on it"""
        if self.entity is None:
            return False
        else:
            return True

    def get_display_char(self):
        """Returns the display character of the tile"""
        return self.display_char

    def get_item(self):
        """Returns the item on the tile"""
        return self.item

    def get_entity(self):
        """Returns the entity on the tile"""
        return self.entity

    def get_walkable(self):
        """Returns the walkability of the tile"""
        return self.walkable

    def set_display_char(self, new_char):
        """Sets the display character of a tile"""
        self.display_char = new_char

    def set_item(self, new_item):
        """Sets the item on the tile"""
        self.item = new_item

    def set_entity(self, new_entity):
        """Sets the entity on the tile"""
        self.entity = new_entity
        if self.entity is not None:
            self.walkable = False
        else:
            self.walkable = True

    def set_walkable(self, is_walkable: bool):
        """Sets the walkability of a tile"""
        self.walkable = is_walkable

