import pytube
from tabulate import tabulate

class Media:
    def __init__(self, n, d, s, u, du, c):
        #properties
        self.name = n
        self.director = d
        self.score = s
        self.url = u
        self.duration = du
        self.cast = c

    #methods
    def show_info(self):
        data = [[self.name, self.director, self.score, self.url, self.duration, self.cast]]

        
        print (tabulate(data))
        # print(self.name, ',', self.director, ',', self.score, ',', self.url, ',', self.duration, ',', self.cast)

    @staticmethod
    def add():
        CAST = []
        name = input("enter movie name: ")
        director = input("enter movie director: ")
        score = input("enter movie score: ")
        url = input("enter download url: ")
        duration = input("enter movie duration (first put an space and enter with this format: 2h16m): ")
        while True:
            Q = input("Do you want to add any cast? (y/n)")
            if Q == "y":
                cast = input("enter cast: ")
                CAST.append(cast)
            else:
                break

        new_movie = Media(name, director, score, url, duration, CAST)
        MOVIES.append(new_movie)
    
    def edit(self):
        
        movie.show_info()
        print("name: 1")
        print("director: 2")
        print("score: 3")
        print("url: 4")
        print("duration: 5")
        print("cast: 6")
        print("EXIT: 7")
        item = int (input("select the item you want to edit or exit: "))
        while True:
            # print ('Select from 1 to 7!')
            # item = int (input("select the item you want to edit: "))
            if item == 1:
                movie.name = input("enter the new name: ")
                print ('Information updated successfully.')
                break
            elif item == 2:
                movie.director = input("enter the new director: ")
                print ('Information updated successfully.')
                break
            elif item == 3:
                movie.score = input("enter the new score: ")
                print ('Information updated successfully.')
                break
            elif item == 4:
                movie.url = input("enter the new url: ")
                print ('Information updated successfully.')
                break
            elif item == 5:
                movie.duration = input("enter the new duration: ")
                print ('Information updated successfully.')
                break
            elif item == 6:
                CAST = []
                while True:
                    Q = input("Do you want to add any cast? (y/n)")
                    if Q == "y":
                        cast = input("enter cast: ")
                        CAST.append(cast)
                    else:
                        break

                movie.cast = CAST
                print ('Information updated successfully.')
                break
            elif item == 7:
                # show_menu()
                break
            else:
                print ('Select from 1 to 7!')
                item = int (input("select the item you want to edit: "))
    
    def remove(self):
        movie.show_info()
        MOVIES.remove(movie)
        print ('The movie has been successfully removed.')

    @staticmethod        
    def search():
        user_input = input ('enter movie name or movie director: ')
        for movie in MOVIES:
            if movie.name == user_input or movie.director == user_input:
                movie.show_info()
                search_result.append(movie)

    def download(self):
        
        # for movie in MOVIES:
        #    if movie.name == name:
                link = movie.url
                first_stream = pytube.YouTube(link).streams.first()
                first_stream.download(output_path='./', filename=movie.name + '.mp4')

    @staticmethod
    def show_list():
        col_names = ["name", "    director", "    score", "      URL", "                           duration", "cast"]
        print(tabulate("",headers= col_names))
        # ("name\t\tdirector\t\tscore\t\turl\t\tduration\t\tcast")
        for movie in MOVIES:
            movie.show_info()


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


class Film(Media):
    def __init__(self, n, d, s, u, du, c, g, bo, rd):
        super().__init__(n, d, s, u, du, c)

        self.genre = g
        self.box_office = bo
        self.release_date = rd
        
class Series(Media):
    def __init__(self, n, d, s, u, du, c, g, nos, noe):
        super().__init__(n, d, s, u, du, c)
        
        self.genre = g
        self.number_of_seasons = nos
        self.number_of_episodes = noe
            
class Documentary(Media):
    def __init__(self, n, d, s, u, du, c, rd):
        super().__init__(n, d, s, u, du, c)

        self.release_date = rd

class Clip(Media):
    def __init__(self, n, d, s, u, du, c, t):
        super().__init__(n, d, s, u, du, c)

        self.topic = t

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


            
db = Database("PyLearn7-Assignment12/database.txt")

MOVIE_NAMES = []
MOVIES = []
ACTORS = []

inception = Media("Inception","Christopher Nolan",14,"https://www.youtube.com/watch?v=herRuccntNE", "2h28m",['Leonardo DiCaprio','Joseph Gordon-Levitt','Cillian Murphy'])
# inception.cast = "Leonardo DiCaprio + Joseph Gordon-Levitt + Cillian Murphy"
dicaprio = Actor('Leonardo DiCaprio', 1974, 'Inception')
dicaprio.show()
dicaprio.movie()
# ACTORS.append(inception.cast)
# print(ACTORS)



def show_menu ():
    print ("1- Add")
    print ("2- Edit")
    print ("3- Remove")
    print ("4- Search")
    print ("5- Download")
    print ("6- Show list")
    print ("7- Exit")

print ("Welcome to my Movie Database application.")
print ("Loading...")

db.read()
print ("Data loaded.")


while True:
    show_menu()
    choice = int(input("enter your choice: "))

    if choice == 1:
        Media.add ()

    elif choice == 2:
        # db.read()
        name = input("enter movie name: ")
        # db.read()
        if name in MOVIE_NAMES:
            for movie in MOVIES:
                # db.read()
                
                if movie.name == name:
                    movie.edit()
                    # db.write()
                    break
        else:
            print("There is no movie with this name in the database.")   
                 
    elif choice == 3:
        name = input("enter movie name: ")
        for movie in MOVIES:
            if movie.name == name:
                movie.remove()

    elif choice == 4:
        search_result = []
        Media.search()
        if len(search_result) == 0:
            print("....not found....")
            

    elif choice == 5:
        name = input("enter movie name: ")
        for movie in MOVIES:
            if movie.name == name:
                movie.download()

    elif choice == 6:
        Media.show_list()

    elif choice == 7:
       
        db.write()
        exit(0)
    else:
        print ("Enter a number between 1 and 7.")
