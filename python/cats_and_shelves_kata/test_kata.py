from unittest import TestCase
import kata as k

class Test(TestCase):
    def test_cats_returnsTheMinimumNumberOfSteepsToReachFinish(self):
        self.assertEqual(2, k.cats(1, 5), "To reach 5 from 1 are needed 2 jumps")
        self.assertEqual(0, k.cats(1, 1), "There are no distances")
        self.assertEqual(2, k.cats(2, 4), "Two jumps are needed to reach 4 from 2")
        self.assertEqual(1, k.cats(3, 6), "Only one jump is needed to reach any shelve with distance exactly three")
        self.assertEqual(270, k.cats(98, 906), "")
