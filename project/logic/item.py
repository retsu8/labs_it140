from ascii_magic import AsciiArt
from json import load

class Item:
    def __init__(self):
        self.items = {
            "research_notes": {
                "name": "Research Notes",
                "description": "Notes of the summon from the lab, all neat and documented.",
                #"item_image": AsciiArt.from_image("images/resaearch_notes.jpg"),
                "location": "meeting_room"
            },
            "green_slime": {
                "name": "Green Slime",
                "description": "A strang glowing green slime that was used in the summon circle?",
                #"item_image": AsciiArt.from_image("images/slime.png"),
                "location": "lab"
            },
            "secret_notes": {
                "name": "Secret Notes",
                "description": "Notes of the issues with the signal that looks like something went wrong.",
                #"item_image": AsciiArt.from_image("images/secret_notes.png"),
                "location": "kira_room"
            },
            "lab_id":{
                "name": "Lab ID",
                "description": "The lab id badge for the lab and grounds",
                #"item_image": AsciiArt.from_image("images/secret_notes.png"),
                "location": "bruce_room"
            },
            "acid": {
                "name": "Acid Vail",
                "description": "Vail of acid placed haphazurdusly on the desk",
                #"item_image": AsciiArt.from_image("images/secret_notes.png"),
                "location": "koal_room"
            },
            "sandwich": {
                "name": "Rye with Tuna",
                "description": "A great lunch to have before setting up the sigals to banish the final boss.",
                #"item_image": AsciiArt.from_image("images/secret_notes.png"),
                "location": "staff_querters"
            },
            "handgun":  {
                "name": "Handgun",
                "description": "Possibly rather useless here but it still helps personal moral.",
                #"item_image": AsciiArt.from_image("images/secret_notes.png"),
                "location": "armory"
            },
            "keys": {
                "name": "Vehicle Keys",
                "description": "Keys for the jeep in the garage.",
                #"item_image": AsciiArt.from_image("images/secret_notes.png"),
                "location": "kitchen"
            },
            "crystals":  {
                "name": "Purple Pulsating Crystal",
                "description": "This crystal is very agitating to be near, best to put it away.",
                #"item_image": AsciiArt.from_image("images/secret_notes.png"),
                "location": "garage"
            }
        }

    def get_item(self, location):
        for key, item in self.items.items():
            if location in item["location"]:
                return self.items[key]
        return ""

    def get_count(self):
        return len(self.items.keys())