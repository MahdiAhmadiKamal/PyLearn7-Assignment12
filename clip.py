from media import Media

class Clip(Media):
    def __init__(self, n, d, s, u, du, c, t):
        super().__init__(n, d, s, u, du, c)

        self.topic = t