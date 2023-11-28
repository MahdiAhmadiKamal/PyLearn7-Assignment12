# import pytube
# from tabulate import tabulate
from media import Media

MOVIE_NAMES = []
MOVIES = []
ACTORS = []


class Database:
    
    def __init__(self, a):
        #properties
        self.address = a

    #methods
    def read(self):

        f = open (self.address, "r")
        
        for line in f:
            result = line.split (",")
            result[len(result)-1] = result[len(result)-1].strip()
            # dict = {"code": result[0], "name": result[1], "price": result[2], "count": result[3]}
            my_obj = Media(result[0], result[1], result[2], result[3], result[4], result[5:len(result):1])
            MOVIES.append(my_obj)
            MOVIE_NAMES.append(result[0])
            ACTORS.append(result[5:len(result):1])
        
        f.close ()
        # return MOVIES
       

    def write(self):
        
        f = open(self.address, "w")
        
        for movie in MOVIES:
            delimiter = ','
            my_string = delimiter.join(movie.cast)

            f.write(movie.name + ",")
            f.write(movie.director + ",")
            f.write(movie.score + ",")
            f.write(movie.url + ",")
            f.write(movie.duration + ",")
            f.write(my_string+'\n')

        f.close ()

# db = Database("PyLearn7-Assignment12/database.txt")