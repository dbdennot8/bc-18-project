import unittest
from dojo import DojoRoomAllocator


class TestsForDojoClassMethods(unittest.TestCase):
    def setUp(self):
        """sets up an instance of the class Dojo, for use in the tests below"""
        self.demo = DojoRoomAllocator()

    def test_can_create_office_and_append_to_appropriate_lists(self):
        """Test whether create_room method can create an office and append as required"""
        self.demo.create_room("office", "NinjaSpace")
        self.assertEqual(len(self.demo.all_offices), 1)

    def test_can_create_living_spaces_and_append_to_appropriate_list(self):
        """Test whether create_room method can create a living space and append as required"""
        self.demo.create_room("livingspace", "NinjaSpace")
        self.assertEqual(len(self.demo.all_living_spaces), 1)

    def test_create_room_takes_only_office_or_living_space_for_room_type(self):
        """Tests that method returns error if room type is not either office, or living space"""
        self.demo.create_room("kitchen", "ya_kwanza")
        self.assertNotEqual(len(self.demo.all_living_spaces), 1)
        self.assertNotEqual(len(self.demo.all_offices), 1)

    def test_create_room_increases_count_of_number_of_rooms(self):
        """Checks that calling the create_room method adds to number of rooms available"""
        initial_room_count = len(self.demo.all_offices)
        self.demo.create_room("office", "ya_kwanza")
        new_room_count = len(self.demo.all_offices)
        self.assertEqual((new_room_count - initial_room_count), 1)

    def test_create_room_does_not_duplicate_room_names_offices(self):
        """Checks that multiple offices are not created having the same name"""
        initial_room_count = len(self.demo.all_office_names)
        self.demo.create_room("office", "ya_kwanza")
        self.demo.create_room("office", "ya_kwanza")
        new_room_count = len(self.demo.all_office_names)
        self.assertNotEqual((new_room_count - initial_room_count), 2)

    def test_create_room_does_not_duplicate_room_names_living_spaces(self):
        """Checks that multiple living spaces are not created having the same name"""
        initial_room_count = len(self.demo.all_living_space_names)
        self.demo.create_room("livingspace", "ya_kwanza")
        self.demo.create_room("livingspace", "ya_kwanza")
        new_room_count = len(self.demo.all_living_space_names)
        self.assertNotEqual((new_room_count - initial_room_count), 2)

    def test_add_person_person_type_only_if_specified_as_either_fellow_or_staff(self):
        """Checks that person_type is specified as either fellow or staff"""
        self.demo.add_person("Kenyan", "Denno", "UleMsee", "Yes")
        self.assertNotEqual(len(self.fellows), 1)
        self.assertNotEqual(len(self.staff), 1)

    def test_add_person_appends_new_person_to_appropriate_list_fellows(self):
        """Check whether fellow is appended to list of fellows"""
        initial_fellows_count = len(self.demo.fellows)
        self.demo.add_person("fellow", "UleMsee", "Denno", "Yes")
        new_fellows_count = len(self.demo.fellows)
        self.assertEqual((new_fellows_count - initial_fellows_count), 1)

    def test_add_person_appends_new_person_to_appropriate_list_staff(self):
        """Check whether staff is appended to list of staff"""
        initial_staff_count = len(self.demo.staff)
        self.demo.add_person("staff", "Ann", "Dela", "N")
        new_staff_count = len(self.demo.staff)
        self.assertEqual((new_staff_count - initial_staff_count), 1)

if __name__ == "__main__":
    unittest.main()
