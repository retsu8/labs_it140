class Player:
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
