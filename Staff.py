"""Sub-class Staff which inherits from class Person
Blueprint for introducing a new Staff to the system."""

class Staff(Person):
    def __init__(self, person_type, first_name, surname, wants_accomodation):
        self.person_type = "Staff"
        self.first_name = first_name
        self.surname = surname
        self.wants_accomodation = "N"
