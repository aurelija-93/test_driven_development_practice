class Room:
    def __init__(self, name):
        self.name = name
        self.song_list = []
        self.guest_list = []

    def add_guest(self, guest):
        self.guest_list.append(guest)

    def remove_guest(self, guest):
        self.guest_list.remove(guest)

    def add_song(self, song):
        self.song_list.append(song)