from ascii_magic import AsciiArt
from json import load


class Map:
    def __init__(self):
        self.location = {
            "start_room": {
                "name": "Start Room",
                "description": "Summoning room for Cthulahu",
                "item": "",
                "room_image": "",
                "connected_rooms": {"west": "lab"},
            },
            "lab": {
                "name": "Lab",
                "description": "Room for resaearch",
                "item": "green_slime",
                "room_image": "",
                "connected_rooms": {
                    "west": "meeting_room",
                    "east": "start_room",
                    "south": "kitchen",
                },
            },
            "meeting_room": {
                "name": "Meeting Room",
                "description": "Room with lots of couches and a few armchairs.",
                "item": "research_notes",
                "room_image": "",
                "connected_rooms": {
                    "east": "lab",
                    "north": "kiras_room",
                    "west": "bruces_room",
                    "south": "koals_room",
                },
            },
            "kiras_room": {
                "name": "Kira's Room",
                "description": "Kira's the lab assistants room. Nice and neat jsut like she was.",
                "item": "secret_notes",
                "room_image": "",
                "connected_rooms": {"south": "meeting_room"},
            },
            "bruces_room": {
                "name": "Bruce's Room",
                "description": "Bruce the lab technician. A very empty room, with almost nothing in it.",
                "item": "lab_id",
                "room_image": "",
                "connected_rooms": {"east": "meeting_room"},
            },
            "koals_room": {
                "name": "Koal's Room",
                "description": "Koal's the lab lead.  Always piled with clutter.",
                "item": "acid",
                "room_image": "",
                "connected_rooms": {"north": "meeting_room"},
            },
            "staff_quarters": {
                "name": "Staff Quarters",
                "description": "Hy! Its the old staff quarters, always feels like home",
                "item": "sandwich",
                "room_image": "",
                "connected_rooms": {
                    "north": "kitchen",
                    "west": "armory",
                    "east": "garage",
                },
            },
            "lounge": {
                "name": "Lounge",
                "description": "I am the being Cthulahu; summoned to this realm.",
                "villian": True,
            },
            "armory": {
                "name": "Armory",
                "description": "Lots of old crates and boxes in here, laboled with everything the research team needed.",
                "item": "handgun",
                "room_image": "",
                "connected_rooms": {"east": "staff_quarters"},
                "locked": "lab_id",
            },
            "kitchen": {
                "name": "Kitchen",
                "description": "Always loved to work in the kitchen, its the closest to the food.",
                "item": "vehicle_keys",
                "room_image": "",
                "connected_rooms": {
                    "north": "lab",
                    "east": "lounge",
                    "south": "staff_quarters",
                },
            },
            "garage": {
                "name": "Garage",
                "description": "There an old jeap in here, wounder if it actually runs.",
                "item": "crystals",
                "room_image": "",
                "connected_rooms": {"east": "staff_quarters"},
                "locked": "acid",
            },
        }

    def get_connected_rooms(self, location):
        return self.location[location]["connected_rooms"]

    def get_description(self, location):
        return self.location[location]["description"]

    def get_name(self, location):
        return self.location[location]["name"]

    def get_villian_location(self):
        for room in self.location:
            if "villian" in self.location[room]:
                return room
