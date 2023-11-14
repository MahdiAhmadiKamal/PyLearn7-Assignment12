from media import Media

class Series(Media):
    def __init__(self, n, d, s, u, du, c, g, nos, noe):
        super().__init__(n, d, s, u, du, c)
        
        self.genre = g
        self.number_of_seasons = nos
        self.number_of_episodes = noe