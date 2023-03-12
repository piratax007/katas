from unittest import TestCase
import board


class Test(TestCase):
    def test_cell_given_a_tuple_like_position_makes_a_cell(self):
        position = (0, 0)
        c = board.Cell(position)
        self.assertIsInstance(c, board.Cell)
        position = (0, 1)
        c = board.Cell(position)
        self.assertIsInstance(c, board.Cell)

    def test_change_color_given_a_color_the_cell_color_change(self):
        position = (0, 0)
        c = board.Cell(position)
        new_color = "black"
        c.change_color(new_color)
        self.assertEqual("black", c.current_color)

        new_color = "white"
        c.change_color(new_color)
        self.assertEqual("white", c.current_color)

    def test_board_give_one_like_the_number_of_rows_and_cols_define_a_board_with_one_cell(self):
        number_of_rows = 1
        number_of_cols = 1

        b = board.Board(number_of_rows, number_of_cols)

        self.assertEqual(1, len(b.grid))
        self.assertEqual(1, len(b.grid[0]))
        self.assertIsInstance(b.grid[0][0], board.Cell)

    def test_board_given_n_rows_and_m_cols_define_a_board_with_n_x_m_cells(self):
        number_of_rows = 1
        number_of_cols = 2
        b = board.Board(number_of_rows, number_of_cols)
        self.assertTrue(all(
            isinstance(b.grid[r][c], board.Cell) for c in range(number_of_cols) for r in range(number_of_rows)
        ))

        number_of_rows = 5
        number_of_cols = 3
        b = board.Board(number_of_rows, number_of_cols)
        self.assertTrue(all(
            isinstance(b.grid[r][c], board.Cell) for c in range(number_of_cols) for r in range(number_of_rows)
        ))

        number_of_rows = 5
        number_of_cols = 5
        b = board.Board(number_of_rows, number_of_cols)
        self.assertTrue(all(
            isinstance(b.grid[r][c], board.Cell) for c in range(number_of_cols) for r in range(number_of_rows)
        ))

    def test_apply_rules_in_a_black_cell_given_East_and_position_1_1_returns_North_and_0_1_like_new_position(self):
        b = board.Board(3, 3)
        ant_direction = "E"
        ant_position = [1, 1]
        b.grid[1][1].current_color = "black"

        new_ant_attributes = b.apply_rules(ant_direction, ant_position)

        self.assertTupleEqual(("N", [0, 1]), new_ant_attributes)
        self.assertEqual("red", b.grid[1][1].current_color)

    def test_apply_rules_in_a_black_cell_given_South_and_position_1_2_returns_East_and_1_3_like_new_position(self):
        b = board.Board(3, 5)
        ant_direction = "S"
        ant_position = [1, 2]
        b.grid[1][2].current_color = "black"

        new_ant_attributes = b.apply_rules(ant_direction, ant_position)

        self.assertTupleEqual(("E", [1, 3]), new_ant_attributes)
        self.assertEqual("red", b.grid[1][2].current_color)

    def test_apply_rules_in_a_black_cell_given_West_and_position_2_1_returns_South_and_3_1_like_new_position(self):
        b = board.Board(4, 2)
        ant_direction = "W"
        ant_position = [2, 1]
        b.grid[2][1].current_color = "black"

        new_ant_attributes = b.apply_rules(ant_direction, ant_position)

        self.assertTupleEqual(("S", [3, 1]), new_ant_attributes)
        self.assertEqual("red", b.grid[2][1].current_color)

    def test_apply_rules_in_a_black_cell_given_North_and_position_0_0_returns_West_and_0_5_like_new_position(self):
        b = board.Board(1, 6)
        ant_direction = "N"
        ant_position = [0, 0]
        b.grid[0][0].current_color = "black"

        new_ant_attributes = b.apply_rules(ant_direction, ant_position)

        self.assertTupleEqual(("W", [0, 5]), new_ant_attributes)
        self.assertEqual("red", b.grid[0][0].current_color)

    def test_apply_rules_in_a_white_cell_given_North_and_position_2_4_returns_East_and_2_0_like_new_position(self):
        b = board.Board(5, 5)
        ant_direction = "N"
        ant_position = [2, 4]
        b.grid[2][4].current_color = "white"

        new_ant_attributes = b.apply_rules(ant_direction, ant_position)

        self.assertTupleEqual(("E", [2, 0]), new_ant_attributes)
        self.assertEqual("black", b.grid[2][4].current_color)

    def test_apply_rules_in_a_white_cell_given_East_and_position_3_0_returns_South_and_0_0_like_new_position(self):
        b = board.Board(4, 1)
        ant_direction = "E"
        ant_position = [3, 0]
        b.grid[3][0].current_color = "white"

        new_ant_attributes = b.apply_rules(ant_direction, ant_position)

        self.assertTupleEqual(("S", [0, 0]), new_ant_attributes)
        self.assertEqual("black", b.grid[3][0].current_color)

    def test_apply_rules_in_a_white_cell_given_South_and_position_0_0_returns_West_and_0_0_like_new_position(self):
        b = board.Board(1, 1)
        ant_direction = "S"
        ant_position = [0, 0]
        b.grid[0][0].current_color = "white"

        new_ant_attributes = b.apply_rules(ant_direction, ant_position)

        self.assertTupleEqual(("W", [0, 0]), new_ant_attributes)
        self.assertEqual("black", b.grid[0][0].current_color)

    def test_apply_rules_in_a_white_cell_given_West_and_position_0_1_returns_North_and_0_1_like_new_position(self):
        b = board.Board(1, 3)
        ant_direction = "W"
        ant_position = [0, 1]
        b.grid[0][1].current_color = "white"

        new_ant_attributes = b.apply_rules(ant_direction, ant_position)

        self.assertTupleEqual(("N", [0, 1]), new_ant_attributes)
        self.assertEqual("black", b.grid[0][1].current_color)

    def test_apply_rules_in_a_red_cell_given_East_and_position_1_1_returns_East_and_1_2_like_new_position(self):
        b = board.Board(3, 3)
        ant_direction = "E"
        ant_position = [1, 1]
        b.grid[1][1].current_color = "red"

        new_ant_attributes = b.apply_rules(ant_direction, ant_position)

        self.assertTupleEqual(("E", [1, 2]), new_ant_attributes)
        self.assertEqual("white", b.grid[1][1].current_color)

    def test_apply_rules_in_a_red_cell_given_South_and_position_1_0_returns_South_and_0_0_like_new_position(self):
        b = board.Board(3, 1)
        ant_direction = "S"
        ant_position = [2, 0]
        b.grid[2][0].current_color = "red"

        new_ant_attributes = b.apply_rules(ant_direction, ant_position)

        self.assertTupleEqual(("S", [0, 0]), new_ant_attributes)
        self.assertEqual("white", b.grid[2][0].current_color)

    def test_apply_rules_in_a_red_cell_given_West_and_position_0_0_returns_West_and_0_0_like_new_position(self):
        b = board.Board(1, 1)
        ant_direction = "W"
        ant_position = [0, 0]
        b.grid[0][0].current_color = "red"

        new_ant_attributes = b.apply_rules(ant_direction, ant_position)

        self.assertTupleEqual(("W", [0, 0]), new_ant_attributes)
        self.assertEqual("white", b.grid[0][0].current_color)

    def test_apply_rules_in_a_red_cell_given_North_and_position_0_1_returns_North_and_0_1_like_new_position(self):
        b = board.Board(1, 3)
        ant_direction = "N"
        ant_position = [0, 1]
        b.grid[0][1].current_color = "red"

        new_ant_attributes = b.apply_rules(ant_direction, ant_position)

        self.assertTupleEqual(("N", [0, 1]), new_ant_attributes)
        self.assertEqual("white", b.grid[0][1].current_color)
