import board


class Ant:
    def __init__(self, h: int, v: int, d: str):
        self.horizontal_position = h
        self.vertical_position = v
        self.current_direction = d
        self.directions = {"E": 0, "N": 1, "O": 2, "S": 3}

    def set_direction(self, cell_state: int):
        translate_direction = {0: "E", 1: "N", 2: "O", 3: "S"}
        if cell_state == 1:
            self.current_direction = translate_direction[(self.directions[self.current_direction] - 1) % 4]
        elif cell_state == 0:
            self.current_direction = translate_direction[(self.directions[self.current_direction] + 1) % 4]
        else:
            pass

    def validate_edges(self, right_boundary: int, bottom_boundary: int):
        if self.horizontal_position < 0 and self.current_direction == "O":
            self.horizontal_position = right_boundary
        elif self.horizontal_position > right_boundary and self.current_direction == "E":
            self.horizontal_position = 0

        if self.vertical_position < 0 and self.current_direction == "N":
            self.vertical_position = bottom_boundary
        elif self.vertical_position > bottom_boundary and self.current_direction == "S":
            self.vertical_position = 0

    def move(self, b: board):
        self.set_direction(b.states[self.vertical_position][self.horizontal_position])
        b.update_cell_state(self)

        if self.current_direction == "E":
            self.horizontal_position += 1
        elif self.current_direction == "N":
            self.vertical_position -= 1
        elif self.current_direction == "O":
            self.horizontal_position -= 1
        else:
            self.vertical_position += 1

        self.validate_edges(b.columns - 1, b.rows - 1)
