class Song():
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["Happy Bday to you,"
                   "I don't want to get hammered",
                   "So I won't drink much"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

happy_bday.sing_song()

bulls_on_parade.sing_song()