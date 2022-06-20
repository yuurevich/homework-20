import pytest
from unittest.mock import MagicMock

from dao.genre import GenreDAO
from dao.model.genre import Genre
from service.genre import GenreService


@pytest.fixture()
def genre_dao():
    genre_dao = GenreDAO(None)

    d1 = Genre(id=1, name='genre1')
    d2 = Genre(id=2, name='genre2')
    d3 = Genre(id=3, name='genre3')

    genre_dao.get_one = MagicMock(return_value=d1)
    genre_dao.get_all = MagicMock(return_value=[d1, d2, d3])
    genre_dao.create = MagicMock(return_value=Genre(id=4, name='genre4'))
    genre_dao.delete = MagicMock()
    genre_dao.update = MagicMock()
    return genre_dao


class TestGenreService:
    @pytest.fixture(autouse=True)
    def genre_service(self, genre_dao):
        self.genre_service =GenreService(dao=genre_dao)

    def test_get_one(self):
        genre = self.genre_service.get_one(1)
        assert genre != None
        assert genre.id != None

    def test_get_all(self):
        genres = self.genre_service.get_all()
        assert len(genres) > 0

    def test_create(self):
        genre_d = {
            "id": 4,
            "name": 'genre4',
        }
        genre = self.genre_service.create(genre_d)
        assert genre.id != None

    def test_delete(self):
        self.genre_service.delete(1)

    def test_update(self):
        genre_d = {
            "id": 3,
            "name": 'new_genre3',
        }
        self.genre_service.update(genre_d)
