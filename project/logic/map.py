from ascii_magic import AsciiArt
from json import load


class Map:
    def __init__(self):
        self.location = {}
        with open("json/map.json", "r") as f:
            self.location = load(f)

    def get_connected_rooms(self, location):
        return  self.location[location]["connected_rooms"]

    def get_description(self, location):
        return self.location[location]["description"]