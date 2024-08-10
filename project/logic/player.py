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
        """Print everwhere the player went"""
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
        """Get the pretty inventory names"""
        inventory = set()
        for item in self.inventory:
            inventory.update([item["name"]])
        return sorted(list(inventory))

    def get_inventory_slug(self):
        """Get the slugs for the inventory"""
        inventory = set()
        for item in self.inventory:
            inventory.update([item["slug"]])
        return sorted(list(inventory))

    def get_inventory_count(self):
        """Count the inventory size"""
        return len(self.inventory)

    def reset(self):
        """Reset the player top defaults to start new game"""
        self.inventory = []
        self.location = "start_room"
        self.visited = []
        self.dead = False
