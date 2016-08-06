# webbrowser module is imported which has open() method
import webbrowser


class Movie():
    """This is a class named 'Movie'

    Method:
       __init__: This is automatically called whenever new instance of class
                 is created
        show_trailer(): This method is called whenever movie poster is clicked
                        It opens respective movie trailer in the web browser

    Attributes:
        self : A reference to current instance
        title (str) : This contains the name/title of movie
        poster_image (str) : This contains poster image of movie
        trailer_youtube (str) : This contains link of movie trailer"""

    def __init__(self, title, poster_image, trailer_youtube):
        self.title = title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)  # Opens a web browser
