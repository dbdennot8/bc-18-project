"""This defines the blueprint for creating an instance of person"""


class Person(object):
    def __init__(self, person_type, first_name, surname, wants_accomodation):
    self.person_type = person_type
    self.first_name = first_name
    self.surname = surname
    self.wants_accomodation = "N"

