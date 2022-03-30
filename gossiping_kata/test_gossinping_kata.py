from unittest import TestCase
import driver as d
import gossiping_kata as gk


class Test(TestCase):
    def test_Driver_given_lesser_than_two_stops_in_the_driver_route_can_not_be_defined_a_driver(self):
        driver_1_route = []
        with self.assertRaises(Exception):
            driver_1 = d.Driver("", driver_1_route)

        driver_1_route = [1]
        with self.assertRaises(Exception):
            driver_1 = d.Driver("", driver_1_route)

    def test_Driver_at_first_stop_the_known_gossips_of_a_driver_is_only_her_own_gossip(self):
        driver_1 = d.Driver("d1", [1, 2])
        known_gossips_driver_1 = driver_1.known_gossips
        expected = {"d1"}
        self.assertEqual(1, driver_1.current_stop)
        self.assertEqual(expected, known_gossips_driver_1)

        driver_2 = d.Driver("d2", [1, 3, 5])
        known_gossips_driver_2 = driver_2.known_gossips
        expected = {"d2"}
        self.assertEqual(1, driver_1.current_stop)
        self.assertEqual(expected, known_gossips_driver_2)

    def test_update_gossips_two_drivers_exchange_gossips(self):
        driver_1 = d.Driver("d1", [2, 1])
        driver_2 = d.Driver("d2", [2, 3])
        driver_1.update_gossips(driver_2)
        self.assertEqual({"d1", "d2"}, driver_1.known_gossips)
        driver_2.update_gossips(driver_1)
        self.assertEqual({"d2", "d1"}, driver_2.known_gossips)

        driver_1 = d.Driver("d1", [1, 2])
        driver_2 = d.Driver("d2", [4, 2, 5])
        driver_2.known_gossips = {"d2", "d3", "d5"}
        driver_1.update_gossips(driver_2)
        self.assertEqual({"d1", "d2", "d3", "d5"}, driver_1.known_gossips)
        driver_2.update_gossips(driver_1)
        self.assertEqual({"d1", "d2", "d3", "d5"}, driver_2.known_gossips)

    def test_simulation_given_an_empty_list_of_drivers_can_not_be_setup_a_simulation(self):
        drivers = []
        with self.assertRaises(Exception):
            s = gk.simulation(drivers)

    def test_simulation_given_less_than_two_drivers_can_not_be_setup_a_simulation(self):
        driver_1 = d.Driver("d1", [1, 2, 3, 4, 5])
        with self.assertRaises(Exception):
            s = gk.simulation([driver_1])

    def test_setup_step_given_a_step_of_the_simulation_perform_the_correspondent_stop_in_each_driver_route(self):
        driver_1 = d.Driver("d1", [2, 1])
        driver_2 = d.Driver("d2", [4, 3, 6, 1, 5, 2])
        s = gk.simulation([driver_1, driver_2])
        s.setup_current_stop(0)
        expected = [2, 4]
        self.assertEqual(expected, [driver_1.current_stop, driver_2.current_stop])

        s.setup_current_stop(2)
        expected = [2, 6]
        self.assertEqual(expected, [driver_1.current_stop, driver_2.current_stop])

        s.setup_current_stop(3)
        expected = [1, 1]
        self.assertEqual(expected, [driver_1.current_stop, driver_2.current_stop])

        s.setup_current_stop(5)
        expected = [1, 2]
        self.assertEqual(expected, [driver_1.current_stop, driver_2.current_stop])

        driver_1 = d.Driver("d1", [5, 1, 2])
        driver_2 = d.Driver("d2", [1, 3, 6, 4, 5, 2, 7])
        driver_3 = d.Driver("d3", [6, 2, 1, 3])
        s = gk.simulation([driver_1, driver_2, driver_3])
        s.setup_current_stop(0)
        expected = [5, 1, 6]
        self.assertEqual(expected, [driver_1.current_stop, driver_2.current_stop, driver_3.current_stop])

        s.setup_current_stop(6)
        expected = [5, 7, 1]
        self.assertEqual(expected, [driver_1.current_stop, driver_2.current_stop, driver_3.current_stop])

    def test_drivers_in_same_stop_given_a_driver_and_a_step_of_the_simulation_returns_the_drivers_in_the_same_stop(self):
        driver_1 = d.Driver("d1", [5, 4, 2])
        driver_2 = d.Driver("d2", [1, 4, 6, 7, 3, 1, 5])
        driver_3 = d.Driver("d3", [6, 1, 5, 3])
        s = gk.simulation([driver_1, driver_2, driver_3])

        expected = []
        actual = s.drivers_in_same_stop(driver_1, 0)
        self.assertEqual(expected, actual)

        expected = [driver_2]
        actual = s.drivers_in_same_stop(driver_1, 1)
        self.assertEqual(expected, actual)

        expected = [driver_3]
        actual = s.drivers_in_same_stop(driver_2, 5)
        self.assertEqual(expected, actual)

        expected = [driver_1, driver_3]
        actual = s.drivers_in_same_stop(driver_2, 6)
        self.assertEqual(expected, actual)

    def test_execute_returns_negative_one_if_the_drivers_never_known_all_the_gossips(self):
        driver_1 = d.Driver("d1", [2, 1, 2])
        driver_2 = d.Driver("d2", [5, 2, 8])
        s = gk.simulation([driver_1, driver_2])

        self.assertEqual(-1, s.execute())

    def test_execute_returns_the_number_of_steps_needed_for_that_all_drivers_knows_all_the_gossips(self):
        driver_1 = d.Driver("d1", [3, 1, 2, 3])
        driver_2 = d.Driver("d2", [3, 2, 3, 1])
        driver_3 = d.Driver("d3", [4, 2, 3, 4, 5])
        s = gk.simulation([driver_1, driver_2, driver_3])

        self.assertEqual(5, s.execute())

        driver_1 = d.Driver("d1", [5, 4, 2])
        driver_2 = d.Driver("d2", [1, 4, 6, 7, 3, 1, 5])
        driver_3 = d.Driver("d3", [6, 1, 5, 3])
        s = gk.simulation([driver_1, driver_2, driver_3])
        self.assertEqual(7, s.execute())
