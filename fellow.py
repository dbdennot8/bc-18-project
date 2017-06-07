from person import Person


class Fellow(Person):
    """Sub-class Fellow which inherits from class Person
    Blueprint for introducing a new Fellow to the system."""
    def __init__(self, person_type, first_name, surname, wants_accommodation="n"):
        super(Fellow, self).__init__(person_type, first_name, surname, wants_accommodation="n")
        self.person_type = "fellow"
        self.first_name = first_name
        self.surname = surname
        self.wants_accommodation = wants_accommodation
