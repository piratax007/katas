from unittest import TestCase
import ant as a


class Test(TestCase):
    def test_ant_given_a_position_and_a_direction_makes_an_ant(self):
        position = [1, 1]
        direction = "N"
        ant = a.Ant(position, direction)
        self.assertIsInstance(ant, a.Ant)

        position = [3, 2]
        direction = "W"
        ant = a.Ant(position, direction)
        self.assertIsInstance(ant, a.Ant)
        
