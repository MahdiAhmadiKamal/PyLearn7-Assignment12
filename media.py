import pytube
from tabulate import tabulate


search_result = []

class Media:
    
    def __init__(self, n, d, s, u, du, c):
        #properties
        self.name = n
        self.director = d
        self.score = s
        self.url = u
        self.duration = du
        self.cast = c
        # return Media

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
        duration = input("enter movie duration (first put an space and enter with this format: 02h06m): ")
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

        search_by = int(input(" search by name: 1 \n search by Running time: 2 \n "))
        if search_by == 1:

            user_input = input ('enter movie name or movie director: ')
            for movie in MOVIES:
                if movie.name == user_input or movie.director == user_input:
                    movie.show_info()
                    search_result.append(movie)

        elif search_by == 2:
                
            print("enter the desired range of movie running time in minute (X to Y minutes): ")
            X = int(input("X: "))
            Y = int(input("Y: "))
                
            for movie in MOVIES:
                hour = int(movie.duration[1:3])
                min = int(movie.duration[4:6])
                total = hour*60 + min
                if X <= total <= Y:
                    movie.show_info()
                    search_result.append(movie)
        else:
            print("select 1 or 2")
            Media.search()
        

    def download(self):
        
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
        