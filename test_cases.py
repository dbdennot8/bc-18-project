import unittest
from Dojo import Dojo


class TestsForCreateRoomMethod(unittest.TestCase):
    def setUp(self):
        self.demo = Dojo()
        """sets up an instance of the class CreateRoom, for use in
		the tests below)"""

    def test_create_room_successfully(self):
        """Tests whether a room is actually created after calling
		the create_room method"""
        office_one = self.demo.create_room("office", "ya_kwanza")
        self.assertTrue(office_one)

    def test_create_room_takes_only_office_or_living_space_for_room_type(self):
        """Tests that method returns error if room type is not either office,
		or living space"""
        with self.assertRaises(AttributeError):
            self.demo.create_room("kitchen", "ya_kwanza")


    def test_create_room_increases_count_of_number_of_rooms(self):
        """Checks that calling the create_room method adds to number of
		rooms available"""
        initial_room_count = len(self.demo.offices) + len(self.demo.living_spaces)
        office_one = self.demo.create_room("office", "ya_kwanza")
        new_room_count = len(self.demo.offices) + len(self.demo.living_spaces)
        self.assertEqual((new_room_count - initial_room_count), 1)

    def test_create_room_takes_only_strings_for_room_names(self):
        with self.assertRaises(ValueError):
            self.demo.create_room("office", 100)


class TestsForAddPerson(unittest.TestCase):
    def setUp(self):
        self.demo = AddPerson()
        """sets up an instance of the class AddPerson, for use in
		the tests below)"""

    def test_add_person_person_type_specified_as_either_fellow_or_staff(self):
        with self.assertRaises(AttributeError):
            self.demo.add_person("Denno UleMsee", "Kenyan")


if __name__ == "__main__":
    unittest.main()
