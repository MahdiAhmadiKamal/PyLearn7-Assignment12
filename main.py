import pytube

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
        print(self.name, ',', self.director, ',', self.score, ',', self.url, ',', self.duration, ',', self.cast)
    
    @staticmethod
    def add():
        name = input("enter movie name: ")
        director = input("enter movie director: ")
        score = input("enter movie score: ")
        url = input("enter download url: ")
        duration = input("enter movie duration: ")
        cast = input("enter cast: ")
        new_movie = Media(name, director, score, url, duration, cast)
        MOVIES.append(new_movie)

    def edit(self):
        name = input ("enter the movie name: ")
        if name in MOVIE_NAMES:
            for movie in MOVIES:
                if self.name == name:
                    self.show_info()
                    print("name: 1")
                    print("director: 2")
                    print("score: 3")
                    print("url: 4")
                    print("duration: 5")
                    print("cast: 6")
                    item = int (input("select the item you want to edit: "))
                    while item != 1 and item != 2 and item != 3 and item != 4 and item != 5 and item != 6:
                        print ('Select from 1 to 6!')
                        item = int (input("select the item you want to edit: "))
                    if item == 1:
                        movie.name = input("enter the new name: ")
                        print ('Information updated successfully.')
                    if item == 2:
                        movie.director = input("enter the new director: ")
                        print ('Information updated successfully.')
                    if item == 3:
                        movie.score = input("enter the new score: ")
                        print ('Information updated successfully.')
                    if item == 4:
                        movie.url = input("enter the new url: ")
                        print ('Information updated successfully.')
                    if item == 5:
                        movie.duration = input("enter the new duration: ")
                        print ('Information updated successfully.')
                    if item == 6:
                        movie.cast = input("enter the new cast: ")
                        print ('Information updated successfully.')
        else:
            print ('There is no movie with this name in the database.')
    
    def remove(self):
        name = input ("enter the movie name: ")
        for movie in MOVIES:
            if movie.name == name:
                self.show_info()
                MOVIES.remove(movie)
                print ('The movie has been successfully removed.')

    @staticmethod        
    def search():
        user_input = input ('type movie name or movie director: ')
        for movie in MOVIES:
            if movie.name == user_input or movie.director == user_input:
                movie.show_info()
                break
        else:
            print ("not found")

    def download(self):
        link = self.url
        first_stream = pytube.YouTube(link).streams.first()
        first_stream.download(output_path='./', filename=self.name +'.mp4')

    def show_list(self):
        print ("name\t\tdirector\t\tscore\t\turl\t\tduration\t\tcast")
        for movie in MOVIES:
            movie.show_info()


class Database(Media):
    def __init__(self, n, d, s, u, du, c):
        super().__init__(n, d, s, u, du, c)
    #methods
    def read(self):
        f = open ("PyLearn7-Assignment12/database.txt", "r")
        
        for line in f:
            result = line.split (",")
            # dict = {"code": result[0], "name": result[1], "price": result[2], "count": result[3]}
            my_obj = Media(result[0], result[1], result[2], result[3], result[4], result[5])
            MOVIES.append (my_obj)
            MOVIE_NAMES.append(my_obj([0]))
            ACTORS.append(my_obj([5]))

        f.close ()
        
    @staticmethod
    def write():
        f = open("PyLearn7-Assignment12/database.txt", "w")
        for movie in MOVIES:
            f.write(movie.name + ",")
            f.write(movie.director + ",")
            f.write(movie.score + ",")
            f.write(movie.url + ",")
            f.write(movie.duration + ",")
            f.write(movie.cast + "\n")

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

class Actor:
    def __init__(self, c):
        #properties
        self.cast = c
    #methods
    def show_cast(self):
        ACTORS.append(self.cast)
        print(ACTORS)
        

db = Database()
MOVIE_NAMES = []
MOVIES = []
ACTORS = []


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
        name = int(input("enter movie name: "))
        for movie in MOVIES:
            if movie.name == name:
                movie.edit()
        
    elif choice == 3:
        name = int(input("enter product name: "))
        for movie in MOVIES:
            if movie.name == name:
                movie.remove()

    elif choice == 4:
        Media.search()

    elif choice == 5:
       Media.download()

    elif choice == 6:
        Media.show_list()
    elif choice == 7:
        db.write()
        exit(0)
    else:
        print ("Enter a number between 1 and 7.")

