from unittest import TestCase


class Test(TestCase):
    def test_user_input(self):
        from rpn_calculator import user_input
        self.assertEqual(user_input("20 5 /"), ["20", "5", "/"], "Should be a list")

    def test_cast(self):
        from rpn_calculator import cast
        self.assertEqual(cast("2"), 2, "Should be 2")
        self.assertEqual(cast("3.14151692"), 3.14151692, "Should be approx PI")
        self.assertEqual(cast("+"), "+", "Should be the string '+'")

    def test_cast_characters(self):
        from rpn_calculator import cast_characters
        self.assertEqual(cast_characters(["20", "5", "/"]), [20, 5, "/"], "The list should contain numbers and "
                                                                          "operators such as strings")

    def test_solver(self):
        from rpn_calculator import solver
        self.assertEqual(solver([20, 5, "/"]), 4, "Should be 4")
        self.assertEqual(solver([4, 2, "+", 3, "-"]), 3, "Should be 3")
        self.assertEqual(solver([3, 5, 8, "*", 7, "+", "*"]), 141, "Should be 141")
        self.assertEqual(solver([16, "SQRT"]), 4, "Should be 4")
        self.assertEqual(solver([2, 9, "SQRT", "+"]), 5, "Should be 5")
