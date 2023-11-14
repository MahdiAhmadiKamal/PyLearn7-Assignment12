from media import Media

class Film(Media):
    def __init__(self, n, d, s, u, du, c, g, bo, rd):
        super().__init__(n, d, s, u, du, c)

        self.genre = g
        self.box_office = bo
        self.release_date = rd