from unittest import TestCase
from board import *

class Test(TestCase):
    def test_cell_given_a_tuple_and_a_color_makes_a_cell(self):
        position = (0, 0)
        color = "red"

        c = Cell(position, color)

        self.assertEqual((0, 0), c.position)
        self.assertEqual("red", c.color)

    def test_change_color_given_a_color_the_cell_color_change(self):
        position = (0, 0)
        color = "red"
        c = Cell(position, color)
        new_color = "black"

        c.change_color(new_color)

        self.assertEqual("black", c.color)


