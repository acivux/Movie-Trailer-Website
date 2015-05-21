__author__ = 'jannie'

import fresh_tomatoes
from media import Movie


# Create movie data
movies = [Movie(
    "Aliens", "A scary movie",
    "http://upload.wikimedia.org/wikipedia/en/thumb/f/fb/Aliens_poster.jpg/220px-Aliens_poster.jpg",
    "https://www.youtube.com/watch?v=hU1YaowhYKM", 5, "R"),
    Movie(
    "Toy Story", "A boy and his zombie toys",
    "http://upload.wikimedia.org/wikipedia/en/thumb/1/13/Toy_Story.jpg/220px-Toy_Story.jpg",
    "https://www.youtube.com/watch?v=vwyZH85NQC4", 3, "G"),
    Movie(
    "Avatar", "A marine on an alien planet",
    "http://upload.wikimedia.org/wikipedia/en/thumb/b/b0/Avatar-Teaser-Poster.jpg/220px-Avatar-Teaser-Poster.jpg",
    "https://www.youtube.com/watch?v=cRdxXPV9GNQ", 2, "PG-13"),
    Movie(
    "School of Rock", "Using rock music to learn",
    "http://upload.wikimedia.org/wikipedia/en/thumb/1/11/School_of_Rock_Poster.jpg/220px-School_of_Rock_Poster.jpg",
    "https://www.youtube.com/watch?v=3PsUJFEBC74", 1, "PG-13"),
    Movie(
    "Ratatouille", "A rat is a chef in Paris",
    "http://upload.wikimedia.org/wikipedia/en/thumb/5/50/RatatouillePoster.jpg/220px-RatatouillePoster.jpg",
    "https://www.youtube.com/watch?v=c3sBBRxDAqk", 4, "G"),
    Movie(
    "Midnight in Paris", "Going back in time to meet Authors",
    "http://upload.wikimedia.org/wikipedia/en/thumb/9/9f/Midnight_in_Paris_Poster.jpg/215px-Midnight_in_Paris_Poster.jpg",
    "https://www.youtube.com/watch?v=BYRWfS2s2v4", 1, "PG-13"),
    Movie(
    "The Goonies", "Kids hunting for treasure",
    "http://upload.wikimedia.org/wikipedia/en/thumb/c/c6/The_Goonies.jpg/220px-The_Goonies.jpg",
    "https://www.youtube.com/watch?v=pWgc8Ute2tU", 4, "PG"),
    Movie(
    "Start Wars IV", "Rebellion grows stronger",
    "http://upload.wikimedia.org/wikipedia/en/thumb/8/87/StarWarsMoviePoster1977.jpg/220px-StarWarsMoviePoster1977.jpg",
    "https://www.youtube.com/watch?v=9gvqpFbRKtQ", 5, "PG")]

# Generate webpage
fresh_tomatoes.open_movies_page(movies)




