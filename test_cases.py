import unittest
from Dojo import Dojo


class TestsForDojoClassMethods(unittest.TestCase):
    def setUp(self):
        """sets up an instance of the class Dojo, for use in the tests below)"""
        self.demo = Dojo()

    def test_can_create_office_and_append_to_appropriate_lists(self):
        """Test whether create_room method can create an office and append as required"""
        self.demo.create_room("office", "NinjaSpace")
        self.assertEqual(len(self.demo.all_offices), 1)

    def test_can_create_living_spaces_and_append_to_appropriate_list(self):
        """Test whether create_room method can create a living space and append as required"""
        self.demo.create_room("living space", "NinjaSpace")
        self.assertEqual(len(self.demo.all_living_spaces), 1)

    def test_create_room_takes_only_office_or_living_space_for_room_type(self):
        """Tests that method returns error if room type is not either office, or living space"""
        with self.assertRaises(AttributeError, msg="Room type must be either office or living space"):
            self.demo.create_room("kitchen", "ya_kwanza")

    def test_create_room_increases_count_of_number_of_rooms(self):
        """Checks that calling the create_room method adds to number of rooms available"""
        initial_room_count = len(self.demo.all_rooms)
        self.demo.create_room("office", "ya_kwanza")
        new_room_count = len(self.demo.all_rooms)
        self.assertEqual((new_room_count - initial_room_count), 1)

    def test_create_room_takes_only_strings_for_room_names(self):
        """Checks that only strings are used for person name"""
        with self.assertRaises(TypeError, msg="Only letters accepted for room name."):
            self.demo.create_room("office", 100)

    def test_add_person_person_type_specified_as_either_fellow_or_staff(self):
        """Checks that person_type is specified as either fellow or staff"""
        with self.assertRaises(AttributeError, msg="Person_type can only either be Fellow or Staff"):
            self.demo.add_person("Kenyan", "Denno", "UleMsee", "Yes")

    def test_add_person_accepts_only_strings_for_person_name(self):
        """Checks that person_name can only be a string"""
        with self.assertRaises(TypeError, msg="Names must be letters only."):
            self.demo.add_person("fellow", "Ulemsee", 100, "Yes")

    def test_add_person_appends_new_person_to_appropriate_list(self):
        """Check whether fellow is appended to list of fellows"""
        initial_fellows_count = len(self.demo.fellows)
        self.demo.add_person("fellow", "Ulemsee", "Denno", "Yes")
        new_fellows_count = len(self.demo.fellows)
        self.assertEqual((new_fellows_count - initial_fellows_count), 1)

    def test_add_person_appends_new_person_to_appropriate_list(self):
        """Check whether staff is appended to list of staff"""
        initial_staff_count = len(self.demo.staff)
        self.demo.add_person("staff", "Ann", "Dela", "N")
        new_staff_count = len(self.demo.staff)
        self.assertEqual((new_staff_count - initial_staff_count), 1)

    def test_add_occupant_method_works(self):
        """Checks that each person added is assigned an office"""
        self.demo.add_person("fellow", "Denno", "UleMsee", "Yes")


    # def test_add_occupant_method_does_not_add_members_to_an_office_past_capacity(self):

    # test allocate room if works
    # allocate only assigns person
    # allocate







if __name__ == "__main__":
    unittest.main()
