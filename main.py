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


    def show_list(self):
        print ("name\t\tdirector\t\tscore\t\turl\t\tduration\t\tcast")
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
            # dict = {"code": result[0], "name": result[1], "price": result[2], "count": result[3]}
            my_obj = Media(result[0], result[1], result[2], result[3], result[4], result[5])
            MOVIES.append (my_obj)
            MOVIE_NAMES.append(result[0])
            ACTORS.append(result[5])

        f.close ()

db = Database("PyLearn7-Assignment12/database.txt")
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

