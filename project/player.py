class Player:
    def __init__(self):
        self.items = []
        self.location = 0
        self.visited = set()

    def update_location(self, location):
        sself.location = location

    def update_items(self, item):
        self.items += [item]

    def get_items(self):
        return self.items

    def get_location(self):
        return self.location
