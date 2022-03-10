class Music:

    def __init__(self, BGM, Originals, SFX, Dub):
        self.BGM = BGM
        self.Originals = Originals
        self.SFX = SFX
        self.Dub = Dub

    def displayTheData(self):
        print("\n" +self.BGM + "\n" +self.Originals + "\n" +self.SFX + "\n" +self.Dub)

class Musician(Music):

    def __init__(self, BGM, Originals, SFX, Dub, Singer, Voice_Artist, Guitarist, Pianist, Tablist, Trumpist):
        self.Singer = Singer
        self.Voice_Artist = Voice_Artist
        self.Guitarist = Guitarist
        self.Pianist = Pianist
        self.Tablist = Tablist
        self.Trumpist = Trumpist

        Music.__init__(self, BGM, Originals, SFX, Dub)

    def getPrintData(self):
        print("Back-Ground =", self.BGM)
        print("Score_Originals =", self.Originals)
        print("Sound_Effects =", self.SFX)
        print("Dubbing =", self.Dub)
        print("Sing =", self.Singer)
        print("Voice Over =", self.Voice_Artist)
        print("Bass =", self.Guitarist)
        print("Tone =", self.Pianist)
        print("Beat =", self.Tablist)
        print("Trumpo =", self.Trumpist)

Music_Outcome = Musician("Yass", "Top Notch", "EDM", "Artist", "Sameer", "Sherlock", "Arijit", "Ani", "Ji", "Howard")

Music_Outcome.getPrintData()

Music_Outcome.displayTheData()