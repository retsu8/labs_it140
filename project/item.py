from json import load


class Item:
    def __init__(self):
        self.items = {}
        with open("json/map.json", "r") as f:
            self.items = load(f)

    def check_item(self, item):
    	if item in self.items