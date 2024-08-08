class Dialogue:
	def __init__(self):
		"""Dialogue functionaity of rooms game; this class makes the dialoge for the game,
			Allowing each function to take care of the specifics for the dialoge assoication.
			Thus only dialoge modiciation should be done here. Incoming var manipulation 
			should kept to a minimum."""
		self.vowels = ("a","e","i","o","u")
		self.help = """To interact with the maps, put go 'direction'.\nTo pickup items, use the command, get item/ or leave item\nTo see this menu again, type in help."""
		self.path = "Choose one of the following paths here {}"
		self.introduction = """Wellcome to Greyhalk, and the tomb of horrors, you're responsible for making it out of this tomb before running into the horrors of Cthulhu. Deep in the crypt, there lies the ancient sigils of summoning.  Having tested these sigals and succeeded; you're now the sole survivor left, after the rest were killed. You need to now collect the various items from the rooms in order to make a new banishing sigal and hopefully it will work.\n"""
	def get_introduciton(self):
		return self.introduction

	def get_player_help(self):
		return self.help

	def get_room_promt(self, location):
		return "Looks like theres only one direction to go here."

	def get_invalid_input(self):
		return "That input is invalid, try again."

	def get_rooms_promt(self, location):
		return """Looks like theres multiple ways to go, where to next?\n_______________________________________________________"""

	def get_additional_input(self):
		return "You can also use 0 to quite the game\n--------------------------------------\n"

	def get_player_died(self):
		return "The game has now ended, you have died."

	def get_item_description(self, item):
		return f"Item Description: {item}"

	def pickup_item(self, item):
		if item[0] in self.vowels:
			return f"You've found an {item}; would you like to pick it up?"
		elif item[-1].lower() == "s":
			return f"Youve found the {item}; would you like to pick it up?"
		return f"Youve found a {item}; would you like to pick it up?"

	def get_room_locked(self, location):
		if "garage" in location:
			return "The room is chained shut, theres not way in."
		elif "armory" in location:
			return "The is locked with a keycard? Maybe there is one around?"

	def leave_item(self):
		return "You decided to leave the item here, this choice may not be wise."

	def pickedup_item(self, item):
		if item[0] in self.vowels:
			return f"You picked up an {item}"
		else:
			return f"You picked up the {item}"

	def get_item_already_found(self, location):
		if location == "garage":
			return "Looks like the truck is empty."
		return "Looks like the room is empty."

	def get_item_pickup(self, item):
		return f"You picked up the item {item}"

	def get_player_inventory(self, inventory_list):
		return f"Inventory: {"; ".join(inventory_list)}"

	def get_room_description(self, description):
		return f"""Description: {description}"""

	def get_player_meets_villan_unarmed(self):
		return "Your not prepared yet, still cant banish back Cthulhu!!!"

	def room_into(self, location):
		return f"""Location: {location}"""