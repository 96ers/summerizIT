import pytest
from faker import Faker

from src.models import User
from src.repositories import BaseRepository

fake = Faker()


class TestBaseRepository:
    @pytest.fixture
    def repository(self, db_session):
        return BaseRepository(model=User, db_session=db_session)

    @pytest.mark.usefixtures
    def test_create(self, repository):
        user = repository.create(self._user_data_geneator())
        repository.session.commit()
        assert user.id is not None

    @pytest.mark.usefixtures
    def test_get_all(self, repository):
        repository.create(self._user_data_generator())
        repository.create(self._user_data_generator())
        users = repository.get_all()
        assert len(users) == 2

    def _user_data_generator(self):
        return {
            "email": fake.email(),
            "username": fake.username(),
            "password": fake.password()
        }
