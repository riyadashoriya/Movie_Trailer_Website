# movie.py file is imported which has Movie() class
import movie
# fresh_tomatoes.py is imported which has open_movies_page() method
import fresh_tomatoes

# An object 'the_proposal' of Movie class is created
the_proposal = movie.Movie("The Proposal",
                           "https://upload.wikimedia.org/wikipedia/en/0/02/The_Proposal.jpg",  # NOQA
                           "https://www.youtube.com/watch?v=RFL8b1p1ELY")

# An object 'taken' of Movie class is created
taken = movie.Movie("Taken",
                    "https://upload.wikimedia.org/wikipedia/en/e/ed/Taken_film_poster.jpg",  # NOQA
                    "https://www.youtube.com/watch?v=pbA-tBrHNfI")

# An object 'pride_and_prejudice' of Movie class is created
pride_and_prejudice = movie.Movie("Pride and Prejudice",
                                  "https://upload.wikimedia.org/wikipedia/en/0/03/Prideandprejudiceposter.jpg",  # NOQA
                                  "https://www.youtube.com/watch?v=1dYv5u6v55Y")  # NOQA

# An object 'cindrella' of Movie class is created
cindrella = movie.Movie("Cindrella",
                        "https://upload.wikimedia.org/wikipedia/en/c/c2/Cinderella_2015_official_poster.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=20DF6U1HcGQ")

# An object 'when_in_rome' of Movie class is created
when_in_rome = movie.Movie("When in Rome",
                           "https://upload.wikimedia.org/wikipedia/en/5/59/When_in_rome_poster.jpg",  # NOQA
                           "https://www.youtube.com/watch?v=gsb8U014Hs0")

# An object 'true_lies' of Movie class is created
true_lies = movie.Movie("True Lies",
                        "https://upload.wikimedia.org/wikipedia/en/4/44/True_lies_poster.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=3B7HG8_xbDw")

# All the objects are group together in the list 'movies'
movies = [the_proposal, taken, pride_and_prejudice, cindrella,
          when_in_rome, true_lies]

# open_movies_page() method of fresh_tomatoes.py is called and
# list of object is passed
fresh_tomatoes.open_movies_page(movies)
