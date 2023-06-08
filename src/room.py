class Room:
    def __init__(self, name, room_limit):
        self.name = name
        self.room_limit = room_limit
        self.song_list = []
        self.guest_list = []

    def check_room_has_space(self):
        return self.room_limit > 0

    def add_guest(self, guest):
        if self.check_room_has_space():
            self.guest_list.append(guest)

    def remove_guest(self, guest):
        self.guest_list.remove(guest)

    def add_song(self, song):
        self.song_list.append(song)

    def check_for_favourite_song(self, guest):
        for song in self.song_list:
            if song.name == guest.favourite_song:
                return guest.whoo()
        return guest.boo()