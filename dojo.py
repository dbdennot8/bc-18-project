"""Central class for the application. Links all the application's dependencies
"""
import random
from office import Office
from living_space import LivingSpace
from fellow import Fellow
from staff import Staff


class DojoRoomAllocator(object):
    """Contains the application's main methods"""
    def __init__(self):
        self.all_offices = []
        self.all_living_spaces = []
        self.all_persons = []
        self.fellows = []
        self.staff = []
        self.all_office_names = []
        self.all_living_space_names = []
        self.allocated_an_office = []
        self.allocated_a_living_space = []

    def create_room(self, room_type, room_name):
        """Creates a new room of given name and type"""
        room_type = room_type.lower()

        if room_type == "office":
            if room_name in self.all_office_names:
                print("A room with this name already exists. Try another name.")
            else:
                new_office = Office(room_type, room_name)
                self.all_office_names.append(room_name)
                self.all_offices.append(new_office)
                print(
                    "The office named {0:s} has been created".format(room_name))

        elif room_type == "livingspace":
            if room_name in self.all_living_space_names:
                print("A room with this name already exists. Try another name.")
            else:
                new_room = LivingSpace(room_type, room_name)
                self.all_living_space_names.append(room_name)
                self.all_living_spaces.append(new_room)
                print(
                    "The living space named {0:s} has been created".format(room_name))
        else:
            print("Room type must be either office or livingspace")

    def add_person(self, person_type, first_name, surname, wants_accommodation="n"):
        """ Method adds a new person and assigns them an office, and an optional living space """
        person_type = person_type.lower()
        wants_accommodation = wants_accommodation.lower()
        if person_type == "fellow" or person_type == "staff":
            if person_type == "fellow":
                new_person = Fellow(person_type, first_name,
                                    surname, wants_accommodation)
                self.all_persons.append(new_person)
                self.fellows.append(new_person)
                print("Fellow {0:s} {1:s} has been successfully added".format(
                    first_name, surname))

                """The following section assigns a random office and an optional random living
                space to the new fellow added above"""
                if len(self.all_offices) == 0:
                    print(
                        "Office not assigned, because no offices are available at this time.")
                else:
                    random_office = random.choice(self.all_offices)
                    if len(random_office.occupants) == 6:
                        random_office = random.choice(self.all_offices)
                    else:
                        random_office.occupants.append(new_person)
                        self.allocated_an_office.append(new_person)
                        print("{0:s} {1:s} has been allocated the office {2:s}".format(
                            new_person.first_name, new_person.surname, random_office.room_name))

                if new_person.wants_accommodation == "yes" or new_person.wants_accommodation == "y":
                    if len(self.all_living_spaces) == 0:
                        print(
                            "Living space not assigned, because no living spaces are available at this time.")
                    else:
                        random_living_space = random.choice(
                            self.all_living_spaces)
                        if len(random_living_space.occupants) == 4:
                            random_living_space = random.choice(self.all_living_spaces)
                        else:
                            random_living_space.occupants.append(new_person)
                            self.allocated_a_living_space.append(new_person)
                            print("{0:s} {1:s} has been allocated the living space {2:s}".format(
                                new_person.first_name, new_person.surname, random_living_space.room_name))

            elif person_type == "staff":
                new_person = Staff(person_type, first_name,
                                   surname, wants_accommodation)
                self.all_persons.append(new_person)
                self.staff.append(new_person)
                print("Staff {0:s} {1:s} has been successfully added".format(
                    first_name, surname))

                if len(self.all_offices) == 0:
                    print(
                        "Office not assigned, because no offices are available at this time.")
                    if new_person.wants_accommodation == "yes" or new_person.wants_accommodation == "y":
                        print("Staff cannot be assigned a living space.")
                else:
                    random_office = random.choice(self.all_offices)
                    if len(random_office.occupants) >= 6:
                        random_office = random.choice(self.all_offices)
                        if new_person.wants_accommodation == "yes" or new_person.wants_accommodation == "y":
                            print("Staff cannot be assigned a living space.")
                    else:
                        random_office.occupants.append(new_person)
                        self.allocated_an_office.append(new_person)
                        print("{0:s} {1:s} has been allocated the office {2:s}".format(new_person.first_name,
                             new_person.surname, random_office.room_name))
                        if new_person.wants_accommodation == "yes" or new_person.wants_accommodation == "y":
                            print("Staff cannot be assigned a living space.")

        else:
            print("Person can only either be Fellow or Staff.")
