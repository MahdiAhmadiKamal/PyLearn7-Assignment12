from media import Media

class Documentary(Media):
    def __init__(self, n, d, s, u, du, c, rd):
        super().__init__(n, d, s, u, du, c)

        self.release_date = rd