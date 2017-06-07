class Room(object):
    """Defines the blueprint for creating an instance of room"""
    def __init__(self, room_type, room_name, max_occupants, occupants=[]):
        self.room_type = room_type
        self.room_name = room_name
        self.max_occupants = max_occupants
        self.occupants = occupants




