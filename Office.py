"""Defines the blueprint for defining a new office"""

from Room import Room
class Office(object):
    def __init__(self, room_name, room_type, max_occupants):
        self.room_name = room_name
        self.room_type = room_type
        self.max_occupants = 6
