class Board:
    def __init__(self, rows: int, cols: int):
        self.rows = rows
        self.cols = cols
        self.grid = [[Cell((r, c)) for c in range(self.cols)] for r in range(self.rows)]
        self.directions = {"E": 0, "N": 1, "W": 2, "S": 3}
        self.translate_direction = {0: "E", 1: "N", 2: "W", 3: "S"}
        self.displacement = {
            "E": (0, 1),
            "N": (-1, 0),
            "W": (0, -1),
            "S": (1, 0)
        }
        self.set_color_displacement = {
            "white": ("black", -1),
            "black": ("red", 1),
            "red": ("white", 0)
        }

    def set_new_direction(self, ant_direction: str, displacement: int) -> str:
        return self.translate_direction[(self.directions[ant_direction] + displacement) % 4]

    def direction_rules(self, current_cell, ant_direction: str) -> str:
        new_ant_direction = \
            self.set_new_direction(ant_direction, self.set_color_displacement[current_cell.current_color][1])
        current_cell.change_color(self.set_color_displacement[current_cell.current_color][0])

        return new_ant_direction

    def boundaries_rules(self, new_ant_direction: str, ant_position: list) -> list:
        if ant_position[0] < 0 and new_ant_direction == "N":
            ant_position[0] = self.rows - 1
            return ant_position

        if ant_position[0] >= self.rows and new_ant_direction == "S":
            ant_position[0] = 0
            return ant_position

        if ant_position[1] < 0 and new_ant_direction == "W":
            ant_position[1] = self.cols - 1
            return ant_position

        if ant_position[1] >= self.cols and new_ant_direction == "E":
            ant_position[1] = 0
            return ant_position

        return ant_position

    def move_rules(self, new_ant_direction: str, ant_position: list) -> list:
        ant_position[0] += self.displacement[new_ant_direction][0]
        ant_position[1] += self.displacement[new_ant_direction][1]

        return self.boundaries_rules(new_ant_direction, ant_position)

    def apply_rules(self, ant_direction: str, ant_position: list) -> (str, list):
        current_cell = self.grid[ant_position[0]][ant_position[1]]

        new_ant_direction = self.direction_rules(current_cell, ant_direction)

        ant_position = self.move_rules(new_ant_direction, ant_position)

        return new_ant_direction, ant_position


class Cell:
    def __init__(self, position: tuple):
        self.position = position
        self.current_color = "black"

    def change_color(self, color: str):
        self.current_color = color
