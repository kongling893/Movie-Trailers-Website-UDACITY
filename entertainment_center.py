#-*- coding:utf-8 -*-
import movies
import fresh_tomatoes
#import MySQLdb
import re


'''Run this file.'''



def valid_url(url):
    '''Used for judging a url is valid or not'''
    return re.match(r'^https?:/{2}\w.+$',url)


class entertainment():
    _command_menu ='''
1.Add a movie.
2.Remove a movie.
3.Show webpage
4.Exit
'''
    def __init__(self):
        self.movies = []
         
    def show_infor(self,s):
        print s


    def switch(self,ch):
        try:
          {'1': lambda : self.add_movie(),
           '2': lambda : self.remove_movie(),
           '3': lambda : self.show_webpage(),
           '4': lambda : self.show_infor("This information should not be presented.")
          }[ch]()
        except KeyError:
          print ("No such a command.")

    def show_webpage(self):
        fresh_tomatoes.open_movies_page(self.movies)
        return

    def add_movie(self):
        movie = self.get_movie()      
        self.movies.append(movie)

    def get_movie(self):
        '''Get a Movie instance from the command input.'''
        movie_data = {}
        print "Input the movie name:"
        movie_data["title"]= raw_input()
        print "Input the storyline:"
        movie_data["storyline"] = raw_input() 
        
        print "Input the youtube trailer url:"
        temp = raw_input()
        while(not valid_url(temp)):
            print "Input a valid youtube trailer url:"
            temp = raw_input()
        movie_data["trailer"] = temp
        
        print "Input the poster url:"
        temp = raw_input()
        while(not valid_url(temp)):
            print "Input a valid poster url:"
            temp = raw_input()
        movie_data["poster"] = temp
        
        movie = movies.Movie(movie_data)
        return movie

    
    def remove_movie(self):
        if len(self.movies) is 0:
            print "We have no movies in database." 
            return   #nothing to be deleted
        print "Now, we have movies:"
        for mv in self.movies:
            print mv.title
        print "Input the name of the movie you want to delete:"
        name = raw_input()
        for i in range(len(self.movies)):
            if self.movies[i].title == name:
                del self.movies[i]   
        return


def main():
    m = entertainment() 
    while(1):
        print entertainment._command_menu
        input_c = raw_input()
        if(input_c is '4'): break
        m.switch(input_c)
        



if __name__ =="__main__":
    main()
    
