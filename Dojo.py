from Office import Office
from living_space import LivingSpace
from Fellow import Fellow
from Staff import Staff
import random


class Dojo(object):
    """Contains the application's main methods"""
    def __init__(self):
        self.all_rooms = []
        self.all_offices = []
        self.available_offices = []
        self.all_living_spaces = []
        self.available_living_spaces = []
        self.all_persons = []
        self.fellows = []
        self.staff = []

    def create_room(self, room_type, room_name):
        if not isinstance(room_name, str):
                raise TypeError("Only letters accepted for room name.")
        elif room_type == "office":
            new_office = Office(room_type, room_name)
            self.all_rooms.append(new_office)
            self.all_offices.append(new_office)
            self.available_offices.append(new_office)
            print(u"The office named {0:s} has been created".format(room_name))

        elif room_type == "living space":
            new_room = LivingSpace(room_type, room_name)
            self.all_rooms.append(new_room)
            self.all_living_spaces.append(new_room)
            self.available_living_spaces.append(new_room)
            print(u"The living space named {0:s} has been created".format(room_name))
        else:
            raise AttributeError("Room type must be either office or living space")

    def add_person(self, person_type, first_name, surname, wants_accommodation):

        if person_type == "fellow":
            new_person = Fellow(person_type, first_name, surname, wants_accommodation)
            self.all_persons.append(new_person)
            self.fellows.append(new_person)
            print(u"Fellow {0:s} {1:s} has been successfully added".format(first_name, surname))
            if len(self.available_offices) <= 0:
                print("Office space is unavailable at this time")
            else:
                random_office = random.choice(self.available_offices)  # Selects a random office from list of
                # available offices
                random_office.add_occupant(new_person)
                print(u"{0:s} has been allocated the office space {1:s}".format(first_name, random_office.room_name))

        elif person_type == "staff":
            new_person = Staff(person_type, first_name, surname)
            self.all_persons.append(new_person)
            self.staff.append(new_person)
            print("Fellow %s %s has been successfully added" % (first_name, surname))

        else:
            raise AttributeError("Person_type can only either be Fellow or Staff")
"""
blue = Dojo()
print(blue.create_room("office", "Green"))
print()
print(blue.add_person("staff", "Dennis", "UleMsee", "No"))
print()
"""








