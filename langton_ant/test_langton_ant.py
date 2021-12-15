from unittest import TestCase


class Test(TestCase):
    def test_ant_set_direction(self):
        import ant as a

        h = a.Ant(0, 0, "N")
        h.set_direction(1)
        self.assertEqual(h.current_direction, "E")

        h1 = a.Ant(3, 2, "S")
        h1.set_direction(2)
        self.assertEqual(h1.current_direction, "S")

        with self.assertRaises(Exception):
            h.set_direction(3)

    def test_ant_validate_edges(self):
        import ant as a

        h = a.Ant(3, 1, "E")
        h.validate_edges(2, 2)
        self.assertEqual(h.horizontal_position, 0)
        self.assertEqual(h.vertical_position, 1)

        h1 = a.Ant(1, 2, "S")
        h1.validate_edges(2, 1)
        self.assertEqual(h1.horizontal_position, 1)
        self.assertEqual(h1.vertical_position, 0)

    def test_ant_move(self):
        import ant as a
        import board as b

        h0 = a.Ant(0, 0, "N")
        b0 = b.Board([[0]])
        h0.move(b0)
        self.assertEqual(h0.horizontal_position, 0)
        self.assertEqual(h0.vertical_position, 0)
        self.assertEqual(b0.states[0][0], 2)

        h1 = a.Ant(1, 0, "E")
        b1 = b.Board([[0, 1, 2]])
        h1.move(b1)
        self.assertEqual(h1.horizontal_position, 1)
        self.assertEqual(h1.vertical_position, 0)
        self.assertEqual(b1.states[0][0], 0)
