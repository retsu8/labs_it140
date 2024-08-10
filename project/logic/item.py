from ascii_magic import AsciiArt
from json import load


class Item:
    def __init__(self):
        self.items = {
            "research_notes": {
                "name": "Research Notes",
                "description": "Notes of the summon from the lab, all neat and documented.",
                # "item_image": AsciiArt.from_image("images/resaearch_notes.jpg"),
                "location": "meeting_room",
                "slug": "research_notes"
            },
            "green_slime": {
                "name": "Green Slime",
                "description": "A strang glowing green slime that was used in the summon circle?",
                # "item_image": AsciiArt.from_image("images/slime.png"),
                "location": "lab",
                "slug": "green_slime"
            },
            "secret_notes": {
                "name": "Secret Notes",
                "description": "Notes of the issues with the signal that looks like something went wrong.",
                # "item_image": AsciiArt.from_image("images/secret_notes.png"),
                "location": "kiras_room",
                "slug": "secret_notes"
            },
            "lab_id": {
                "name": "Lab ID",
                "description": "The lab id badge for the lab and grounds",
                # "item_image": AsciiArt.from_image("images/secret_notes.png"),
                "location": "bruces_room",
                "slug": "lab_id"
            },
            "acid": {
                "name": "Acid Vail",
                "description": "Vail of acid placed haphazurdusly on the desk",
                # "item_image": AsciiArt.from_image("images/secret_notes.png"),
                "location": "koals_room",
                "slug": "acid"
            },
            "sandwich": {
                "name": "Rye with Tuna",
                "description": "A great lunch to have before setting up the sigals to banish the final boss.",
                # "item_image": AsciiArt.from_image("images/secret_notes.png"),
                "location": "staff_quarters",
                "slug": "sandwich"
            },
            "handgun": {
                "name": "Handgun",
                "description": "Possibly rather useless here but it still helps personal moral.",
                # "item_image": AsciiArt.from_image("images/secret_notes.png"),
                "location": "armory",
                "slug": "handgun"
            },
            "keys": {
                "name": "Vehicle Keys",
                "description": "Keys for the jeep in the garage.",
                # "item_image": AsciiArt.from_image("images/secret_notes.png"),
                "location": "kitchen",
                "slug": "keys"
            },
            "crystals": {
                "name": "Purple Pulsating Crystal",
                "description": "This crystal is very agitating to be near, best to put it away.",
                # "item_image": AsciiArt.from_image("images/secret_notes.png"),
                "location": "garage",
                "slug": "crystals"
            },
        }

    def get_item(self, location):
        for key, item in self.items.items():
            if location in item["location"]:
                return self.items[key]
        return ""

    def get_count(self):
        return len(self.items.keys())

    def get_description(self, item):
        return self.items[item]["description"]
