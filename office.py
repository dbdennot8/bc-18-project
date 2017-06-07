from room import Room


class Office(Room):
    """Defines the blueprint for defining a new office"""
    def __init__(self, room_type, room_name, max_occupants=6, occupants=[]):
        super(Office, self).__init__(room_type, room_name, max_occupants=6, occupants=[])
        self.room_type = "office"
        self.room_name = room_name
        self.max_occupants = max_occupants
        self.occupants = occupants


