import webbrowser



class Movie():
    '''The class define the format of a movie'''
    valid_ratings = ["G","PG","PG-13","R"]
    
    def __init__(self,movie_data):
        self.title = movie_data["title"]
        self.storyline = movie_data["storyline"]
        self.trailer_youtube_url = movie_data["trailer"]
        self.poster_image_url = movie_data["poster"]

    def show_trailer(self):
        webbrowser.open(trailer_youtube_url)
        

