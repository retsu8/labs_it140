from json import load


class Map:
    def __init__(self):
        self.location = {}
        with open("json/map.json", "r") as f:
            self.location = load(f)
