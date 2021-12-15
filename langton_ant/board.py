import ant


class Board:
    def __init__(self, s: list):
        self.states = s
        self.rows = len(s)
        self.columns = len(s[0])
        self.state_switch = {0: 2, 1: 0, 2: 1}

    @staticmethod
    def printable_board(self, a: ant):
        printable_board = [[" _" + str(self.states[i][j]) for j in range(self.columns)] for i in range(self.rows)]
        printable_board[a.vertical_position][a.horizontal_position] = \
            printable_board[a.vertical_position][a.horizontal_position].replace("_", a.current_direction)

        return printable_board

    def update_cell_state(self, a: ant):
        self.states[a.vertical_position][a.horizontal_position] = \
            self.state_switch[self.states[a.vertical_position][a.horizontal_position]]

        self.printable_board(self, a)

    def draw(self, a: ant):
        align_factor = len(str(self.rows))

        print(" " * align_factor + "-" * (self.columns * 3 + 3))
        print(*[f"{i:>{align_factor}}|" + "".join(self.printable_board(self, a)[i]) + " |" for i in range(self.rows)],
              sep='\n')
        print(" " * align_factor + "-" * (self.columns * 3 + 3))
