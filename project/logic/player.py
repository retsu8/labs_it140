class Player:
    """Class building the basic player setup"""
    def __init__(self):
        self.inventory = []
        self.location = "start_room"
        self.visited = set()
        self.dead = False

    def update_location(self, location):
        sself.location = location

    def update_items(self, item):
        self.items += [item]

    def get_items(self):
        return self.items

    def get_location(self):
        return self.location

    def pickup_item(self, item):
        self.inventory += [item]
        return self.inventory

    def get_inventory(self):
        inventory = set()
        for item in self.inventory:
            inventory.update([item["name"]])
        return list(inventory)     

    def get_inventory_count(self):
        return len(self.inventory)

    def reset(self):
        self.inventory = []
        self.location = "start_room"
        self.visited = set()
        self.dead = False