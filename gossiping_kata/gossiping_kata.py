class simulation():
    def __init__(self, drivers: list):
        if len(drivers) < 2:
            raise Exception("with less than two drivers can't be perform a simulation")

        self.drivers = drivers

    def setup_current_stop(self, step: int):
        for driver in self.drivers:
            if step >= len(driver.route):
                driver.current_stop = driver.route[step % len(driver.route)]
            else:
                driver.current_stop = driver.route[step]

    def drivers_in_same_stop(self, driver, step: int) -> list:
        rest_drivers = self.drivers.copy()
        rest_drivers.remove(driver)
        self.setup_current_stop(step)
        return [d for d in filter(lambda d: d.current_stop == driver.current_stop, rest_drivers)]

    def execute(self) -> int:
        step = 0
        while True:
            for driver in self.drivers:
                coincidents = self.drivers_in_same_stop(driver, step)
                if coincidents:
                    for d in coincidents:
                        driver.update_gossips(d)
                        d.update_gossips(driver)
                else:
                    continue

            drivers_with_all_gossips = all(len(d.known_gossips) == len(self.drivers) for d in self.drivers)

            if drivers_with_all_gossips:
                return step + 1
            elif step < 481:
                step += 1
            else:
                return -1



# ToDo
# - Un objeto driver que tenga la lista de gossips conocidos ✓
# - Un método del objeto driver que intercambie los chismes ✓
# - Un método del objeto simulation que determine qué parada debe leerse en los drivers en un paso dado de la simulación ✓
# - Un método del objeto simulation que determine cuándo dos o más drivers coinciden en la misma parada ✓
# - Un método del objeto simulación que ejecute la simulación hasta que todos los drivers conozcan todos
#   los chismes o hasta determinal que nunca sucederá ✓