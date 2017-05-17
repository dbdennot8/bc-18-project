from person import Person


class Staff(Person):
    """Sub-class Staff which inherits from class Person
    Blueprint for introducing a new Staff to the system."""
    def __init__(self, person_type, first_name, surname, wants_accommodation="N"):
        super(Staff, self).__init__(person_type, first_name, surname)
        self.person_type = "staff"
        self.first_name = first_name
        self.surname = surname
        self.wants_accommodation = wants_accommodation
