import vector2d

class map:
    def __init__(self, tile_width, map_array) -> None:
        self.tile_width = tile_width
        self.map_array = map_array

    def is_colliding(self, position : vector2d):
        position.x %= self.tile_width
        position.y %= self.tile_width

        if (self.map_array[position.y][position.x] == 0):
            return True
        
        return False