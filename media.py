__author__ = 'jannie'

import webbrowser


class Movie():
    """Class for storing movie information."""

    # The values for this dictionary must match the CSS class names in the generated HTML
    VALID_MPAA_RATINGS = {"G": "ribbon-green",
                          "PG": "ribbon-blue",
                          "PG-13": "ribbon-blue",
                          "R": "ribbon-orange",
                          "NC-17": "ribbon-red"}

    def __init__(self,
                 movie_title,
                 movie_storyline,
                 movie_poster,
                 movie_trailer,
                 movie_viewer_rating,
                 movie_mpaa_rating):
        """Constructor for the Movie class.

        Sets up the instance of the class with the supplied values.
        Only limited error checking is done to ensure clean execution.

        Args:
             movie_title: Title of the flick
             movie_storyline: Short story line
             movie_poster: URL pointing to the movie poster
             movie_trailer: URL pointing to the movie trailer video
             movie_viewer_rating: Viewer rating, 1-5
             movie_mpaa_rating: The MPAA rating, matching VALID_MPAA_RATINGS
        """

        # MPAA rating is required
        assert movie_mpaa_rating in self.VALID_MPAA_RATINGS.keys(), "MPAA rating missing or not correct: %s" % movie_title

        # Viewer rating validation
        assert 0 < movie_viewer_rating < 6, "Viewer rating must be between 1 and 5: %s" % movie_title

        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = movie_poster
        self.trailer_youtube_url = movie_trailer
        self.viewer_rating = movie_viewer_rating
        self.mpaa_rating = movie_mpaa_rating
        self.mpaa_rating_style = self.VALID_MPAA_RATINGS[movie_mpaa_rating]

    def show_trailer(self):
        """Opens a web browser to the movie trailer URL."""
        webbrowser.open_new(self.trailer)
