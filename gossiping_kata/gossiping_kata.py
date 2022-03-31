class Simulation:
    def __init__(self, drivers: list):
        if len(drivers) < 2:
            raise Exception("with less than two drivers can't be perform a simulation")

        self.drivers = drivers

    def setup_current_stop(self, minute: int):
        for driver in self.drivers:
            driver.current_stop = driver.route[minute % len(driver.route)]

    def rest_drivers(self, driver) -> list:
        rd = self.drivers.copy()
        rd.remove(driver)
        return rd

    @staticmethod
    def filter_drivers_by_stop(stop: int, drivers_to_filter: list) -> list:
        return list(filter(lambda d: d.current_stop == stop, drivers_to_filter))

    def drivers_at_same_stop(self, driver, minute: int) -> list:
        self.setup_current_stop(minute)
        rd = self.rest_drivers(driver)
        return self.filter_drivers_by_stop(driver.current_stop, rd)

    def exchange_gossips(self, driver, minute):
        for d in self.drivers_at_same_stop(driver, minute):
            driver.add_unknown_gossips(d)
            d.add_unknown_gossips(driver)

    def has_all_drivers_all_gossips(self) -> bool:
        return all(len(d.known_gossips) == len(self.drivers) for d in self.drivers)

    def execute(self) -> int:
        minute = 0
        while True:
            for driver in self.drivers:
                self.exchange_gossips(driver, minute)

            if self.has_all_drivers_all_gossips():
                return minute + 1
            elif minute < 481:
                minute += 1
            else:
                return -1
