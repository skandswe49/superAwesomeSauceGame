import vector2d

class map:
    def __init__(self, tile_width : int, map_array : list[list[int]]) -> None:
        self.tile_width = tile_width
        self.map_array = map_array

    def is_colliding(self, position : vector2d):
        x = int(position.x / self.tile_width)
        y = int(position.y / self.tile_width)

        if ((x or y) < 0):
            return True
        elif (x > len(self.map_array[0]) or y > len(self.map_array)):
            return True

        if (self.map_array[x][y] == 0):
            return False
        else:
            return True