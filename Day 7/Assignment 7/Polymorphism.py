class Singing:

    def song(self):
        print("All Singers Select their Own Versatile Songs for Singing")

class Melody(Singing):

    def song(self):
        super().song()
        print("Melody Singers has their Own Versatile of Singing")

Singer = Melody()

Singer.song()