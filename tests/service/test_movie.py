import pytest
from unittest.mock import MagicMock

from dao.movie import MovieDAO
from dao.model.movie import Movie
from service.movie import MovieService


@pytest.fixture()
def movie_dao():
    movie_dao = MovieDAO(None)

    m1 = Movie(id=1, title='title1', description='description1', trailer='trailer1', year=2022,
               rating=7.5, genre_id=1, director_id=2)
    m2 = Movie(id=2, title='title2', description='description2', trailer='trailer2', year=2021,
               rating=8.5, genre_id=2, director_id=2)
    m3 = Movie(id=3, title='title3', description='description3', trailer='trailer3', year=2020,
               rating=9.5, genre_id=3, director_id=3)

    movie_dao.get_one = MagicMock(return_value=m1)
    movie_dao.get_all = MagicMock(return_value=[m1, m2, m3])
    movie_dao.create = MagicMock(return_value=Movie(id=4, title='title4', description='description4',
                                                    trailer='trailer4', year=2019,
                                                    rating=8, genre_id=4,
                                                    director_id=4))
    movie_dao.delete = MagicMock()
    movie_dao.update = MagicMock()
    return movie_dao


class TestMovieService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        self.movie_service = MovieService(dao=movie_dao)

    def test_get_one(self):
        movie = self.movie_service.get_one(1)
        assert movie != None
        assert movie.id != None

    def test_get_all(self):
        movies = self.movie_service.get_all()
        assert len(movies) > 0

    def test_create(self):
        movie_d = {
            'title': 'title4',
            'description': 'description4',
            'trailer': 'trailer4',
            'year': 2019,
            'rating': 8,
            'genre_id': 4,
            'director_id': 4
        }
        movie = self.movie_service.create(movie_d)
        assert movie.id != None

    def test_delete(self):
        self.movie_service.delete(1)

    def test_update(self):
        movie_d = {
            'id': 3,
            'title': 'new_title3',
            'description': 'new_description3',
            'trailer': 'new_trailer3',
            'year': 2022,
            'rating': 9,
            'genre_id': 2,
            'director_id': 2
        }
        self.movie_service.update(movie_d)
