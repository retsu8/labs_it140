from ascii_magic import AsciiArt
from player import Player


class Map:
    def __init__(self):
        self.location = {
            "Lab": {
                "disciption": "Room for resaearch",
                "item": "same of organizims on signal",
                "item_image": AsciiArt.from_image(
                    "images/pixel-art-green-potion-icon-png.png"
                ),
            }
        }


map = Map()
print(map.location["Lab"]["item_image"].to_terminal())
