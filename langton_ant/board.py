from random import randint
import ant


class Board:
    def __init__(self, s: list):
        self.states = s
        self.rows = len(s)
        self.columns = len(s[0])
        self.state_switch = {0: 2, 1: 0, 2: 1}

    @staticmethod
    def printable_board(self, walker: ant):
        printable_board = [[" _" + str(self.states[i][j]) for j in range(self.columns)] for i in range(self.rows)]
        printable_board[walker.vertical_position][walker.horizontal_position] = printable_board[walker.vertical_position][walker.horizontal_position].replace("_", walker.current_direction)

        return printable_board

    def update_states(self, walker: ant):
        if self.states[walker.vertical_position][walker.horizontal_position] == 1:
            self.states[walker.vertical_position][walker.horizontal_position] = 0
        elif self.states[walker.vertical_position][walker.horizontal_position] == 0:
            self.states[walker.vertical_position][walker.horizontal_position] = 2
        else:
            self.states[walker.vertical_position][walker.horizontal_position] = 1

        self.printable_board(self, walker)

    def draw(self, hormiga: ant):
        align_factor = len(str(self.rows))

        print(" " * align_factor + "-" * (self.columns * 3 + 3))
        print(*[f"{i:>{align_factor}}|" + "".join(self.printable_board(self, hormiga)[i]) + " |" for i in range(self.rows)], sep='\n')
        print(" " * align_factor + "-" * (self.columns * 3 + 3))
