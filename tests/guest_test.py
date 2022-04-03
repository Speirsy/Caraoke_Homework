import unittest
from src.rooms import Rooms
from src.guests import Guest
from src.songs import Songs

class TestGuests(unittest.TestCase):

    def setUp(self):
        
        self.guests_1 = Guest("Jim", 33, 10)
        self.guests_2 = Guest("Bill", 35, 10)
        self.guests_3 = Guest("Lisa", 34, 10)
        

    def test_guests_have_a_group(self):
        self.assertEqual("Jim", self.guests_1.name)
        # self.assertEqual("Jack", self.guest_2.name) #AssertionError: 'Jack' != 'Abi'
        self.assertEqual("Bill", self.guests_2.name)

    def test_guests_have_age(self):
        self.assertEqual(35, self.guests_2.age)    

    def test_guests_have_cash(self):
        self.assertEqual(10, self.guests_3.wallet)






             # def test_guests_can_afford_room(self):
    #     self.guests.rent_room(room)
    #     self.assertEqual(self.guests_6.wallet)