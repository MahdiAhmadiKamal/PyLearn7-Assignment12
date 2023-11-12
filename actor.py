class Actor():
    def __init__(self, n, b, c):
        #properties
        self.name = n
        self.birth_year = b
        self.birth_country = c
    #methods
    def show(self):
        print("name:", self.name, "  born:", self.birth_year, "  birth country:", self.birth_country)

    def movie(self):
        f = open ("PyLearn7-Assignment12/database.txt", "r")
        actor_movies=[]
        
        for line in f:
            result = line.split (",")
            
            movie = result[0]
            actors = result[5:len(result):1]
            
            if self.name in actors:
                actor_movies.append(movie)

        print(actor_movies)
        f.close()