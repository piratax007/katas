class Driver:
    def __init__(self, own_gossip: str, route: list):
        self.own_gossip = own_gossip
        self.known_gossips = {own_gossip}
        if len(route) > 1:
            self.route = route
        else:
            raise Exception("at least two stops must be in the route")
        self.current_stop = self.route[0]

    def update_gossips(self, other_driver) -> set:
        for gossip in other_driver.known_gossips:
            self.known_gossips.add(gossip)
