from media import Media         
from database import Database
from database import MOVIES
from database import MOVIE_NAMES
from actor import Actor

# MOVIE_NAMES = []
# MOVIES = []
# ACTORS = []

db = Database("PyLearn7-Assignment12/database.txt")

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
        new_movie = Media.add()
        MOVIES.append(new_movie)

    elif choice == 2:
        name = input("enter movie name: ")
    
        if name in MOVIE_NAMES:
            for movie in MOVIES:
                
                if movie.name == name:
                    Media.edit(movie)
                    break
        else:
            print("There is no movie with this name in the database.")   
                 
    elif choice == 3:
        name = input("enter movie name: ")
        for movie in MOVIES:
            if movie.name == name:
                Media.remove(MOVIES, movie)

    elif choice == 4:
        search_result = []
        Media.search(MOVIES)
        found_movie=Media.search
        search_result.append(found_movie)
        if len(search_result) == 0:
            print("....not found....")
            

    elif choice == 5:
        name = input("enter movie name: ")
        for movie in MOVIES:
            if movie.name == name:
                Media.download(movie)

    elif choice == 6:
        Media.show_list(MOVIES)

    elif choice == 7:
        
        db.write()
        exit(0)
    else:
        print ("Enter a number between 1 and 7.")