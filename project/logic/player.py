class Player:
    """Class building the basic player setup"""

    def __init__(self):
        """__init__ function of player class to build player"""
        self.inventory = []
        self.location = "start_room"
        self.visited = []
        self.dead = False

    def update_location(self, location):
        """set the location of the player in the map"""
        self.location = location
        self.visited += [location]

    def get_visited_map(self):
        return self.visited

    def update_items(self, item):
        """Add items to inventory"""
        self.items += [item]

    def get_location(self):
        """Get the players location"""
        return self.location

    def pickup_item(self, item):
        """Get item add to inventory items"""
        self.inventory += [item]
        return self.inventory

    def get_inventory(self):
        inventory = set()
        for item in self.inventory:
            inventory.update([item["name"]])
        return sorted(list(inventory))

    def get_inventory_count(self):
        return len(self.inventory)

    def reset(self):
        self.inventory = []
        self.location = "start_room"
        self.visited = []
        self.dead = False
