"""Defines the blueprint for creating a new LivingSpace"""

from Room import Room
class LivingSpace(Room):
    def __init__(self, room_name, room_type, max_occupants):
        self.room_name = room_name
        self.room_type = "office"
        self.max_occupants = 4
