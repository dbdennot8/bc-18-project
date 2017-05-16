"""Defines the blueprint for creating an instance of room"""


class Room(object):
	def __init__(self, room_type, room_name, occupants):
		self.room_type = room_type
		self.room_name = room_name
		self.occupants = occupants

	def allocate_room(self):
		pass