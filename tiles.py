class Tile:
    """
    Defines what a tile is, as well as its methods.
    """
    def __init__(self, display_char=' ', item=None, entity=None):
        self.display_char = display_char
        self.item = item
        self.entity = entity
        self.walkable = True

    def get_display_char(self):
        return self.display_char

    def set_display_char(self, new_char):
        self.display_char = new_char

    def set_item(self, new_item):
        self.item = new_item

    def set_entity(self, new_entity):
        self.entity = new_entity

    def set_walkable(self, is_walkable: bool):
        self.walkable = is_walkable

