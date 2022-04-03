class Rooms:

    def __init__(self, number, capacity, price):

        self.name = number
        self.capacity = capacity
        self.price = price
        self.room_guests = []
        self.room_songs = []


    def guest_count(self):
        return len(self.room_guests)

    def song_count(self):
        return len(self.room_songs) 

    def check_in_guest(self, guest):
        self.room_guests.append(guest)













