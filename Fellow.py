"""Sub-class Fellow which inherits from class Person
Blueprint for introducing a new Fellow to the system."""

class Fellow(Person):
    def __init__(self, person_type, first_name, surname, wants_accomodation):
        self.person_type = "Fellow"
        self.first_name = first_name
        self.surname = surname
        self.wants_accomodation = "N"
