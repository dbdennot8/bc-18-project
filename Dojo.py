"""The class containing links the methods run by the application"""

from Office import Office
from living_space import LivingSpace
from Fellow import Fellow
from Staff import Staff

class Dojo(object):
    def __init__(self, all_rooms, offices, living_spaces, all_persons,
                 fellows, staff, allocated_rooms, unallocated_rooms)
        self.all_rooms = []
        self.offices = []
        self.living_spaces = []
        self.all_persons =[]
        self.fellows = []
        self.staff = []
        self.allocated_rooms = []
        self.unallocated_rooms = []

    def create_room(self):
        if room_type = "office":
            new_office = ("Office", (room_name))
            self.offices.append(new_office)
            self.unallocated_rooms.append(new_office)
        elif room_type = "living space":
            new_living_space = ("Living Space", (room_name))
            self.living_spaces.append(new_living_space)
            self.unallocated_rooms.append(new_living_space)


