from ascii_magic import AsciiArt
from json import load

class Item:
    def __init__(self):
        self.items = {}
        with open("json/map.json", "r") as f:
            self.items = load(f)

    def get_item(self, location):
        