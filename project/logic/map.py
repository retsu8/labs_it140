from ascii_magic import AsciiArt
from json import load


class Map:
    def __init__(self):
        self.location = {
            "start_room": {
                "description": "Summoning room for Cthulahu",
                "item": "",
                "room_image": "",
                "connected_rooms": ["lab"]
            },
            "lab": {
                "description": "Room for resaearch",
                "item": "green_slime",
                "room_image": "",
                "connected_rooms": ["meeting_room", "start_room", "kitchen"] 
            },
            "meeting_room": {
                "description": "Group Room",
                "item": "research_notes",
                "room_image": "",
                "connected_rooms": ["lab", "kira_room", "bruce_room", "koal_room"] 
            },
            "kira_room": {
                "description": "Kira's the lab assistants room. Nice and neat jsut like she was.",
                "item": "secret_notes",
                "room_image": "",
                "connected_rooms": ["meeting_room"] 
            },
            "bruce_room": {                
                "description": "Bruce the lab technician. A very empty room, with almost nothing in it.",
                "item": "lab_id",
                "room_image": "",
                "connected_rooms": ["meeting_room"]
            },
            "koal_room": {
                "description": "Koal's the lab lead.  Always piled with clutter.",
                "item": "acid",
                "room_image": "",
                "connected_rooms": ["meeting_room"]
            },
            "staff_querters": {
                "description": "Hy! Its the old staff quarters, always feels like home",
                "item": "sandwich",
                "room_image": "",
                "connected_rooms": ["kitchen", "armory", "garage"]
            },
            "lounge": {
                "description": "I am the being Cthulahu; summoned to this realm.",
                "villian": True
            },
            "armory": {
                "description": "Lots of old crates and boxes in here, laboled with everything the research team needed.",
                "item": "handgun",
                "room_image": "",
                "connected_rooms": ["staff_querters"],
                "locked": "lab_id"
            },
            "kitchen": {
                "description": "Always loved to work in the kitchen, its the closest to the food.",
                "item": "vehicle_keys",
                "room_image": "",
                "connected_rooms": ["lab", "lounge", "staff_querters"]
            },
            "garage": {
                "description": "There an old jeap in here, wounder if it actually runs.",
                "item": "crystals",
                "room_image": "",
                "connected_rooms": ["staff_querters"],
                "locked": "acid"
            }
        }

    def get_connected_rooms(self, location):
        return  self.location[location]["connected_rooms"]

    def get_description(self, location):
        return self.location[location]["description"]

    def get_villian_location(self):
        for room in self.location:
            if "villian" in self.location[room]:
                return room