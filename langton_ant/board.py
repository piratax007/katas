from random import randint
import ant


class Board:
    def __init__(self, r: int, c: int):
        self.rows = r
        self.columns = c
        self.grid = [[randint(0, 1) for _ in range(self.columns)] for _ in range(self.rows)]

    def set_cell_state(self, walker: ant):
        if self.grid[walker.vertical_position][walker.horizontal_position] != 0:
            self.grid[walker.vertical_position][walker.horizontal_position] = 0
        else:
            self.grid[walker.vertical_position][walker.horizontal_position] = 1

    def draw(self):
        for row in range(self.rows):
            print(self.grid[row], sep="\n")
