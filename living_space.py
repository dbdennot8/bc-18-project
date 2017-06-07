from room import Room


class LivingSpace(Room):
    """Defines the blueprint for creating a new Living Space"""
    def __init__(self, room_type, room_name, max_occupants=4, occupants=[]):
        super(LivingSpace, self).__init__(room_type, room_name, max_occupants=4, occupants=[])
        self.room_type = "living space"
        self.room_name = room_name
        self.max_occupants = max_occupants
        self.occupants = occupants

