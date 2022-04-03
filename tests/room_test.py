import unittest
from src.rooms import Rooms
from src.guests import Guest
from src.songs import Songs

class TestRooms(unittest.TestCase):

    def setUp(self):
    
        self.room_1 = Rooms("one", 5, 5)
        self.room_2 = Rooms("two", 9, 10)
        self.room_3 = Rooms("three", 13, 15)

        self.guests_1 = Guest("Jim", 33, 10)
        self.guests_2 = Guest("Bill", 35, 10)
        self.guests_3 = Guest("Lisa", 34, 10)


    def test_room_has_a_name(self):
        self.assertEqual("one", self.room_1.name)    


    def test_room_has_a_price(self):
        self.assertEqual(10, self.room_2.price)

    def test_guest_check_in(self):
        self.rooms.check_in_guest(self.guests_1)
        self.assertEqual(1, self.rooms.guest_count())