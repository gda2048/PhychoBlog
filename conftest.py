import pytest
import dj_database_url
from decouple import config
from psycho import settings


@pytest.fixture(scope='session')
def django_db_setup():
    settings.DATABASES['default'] = dj_database_url.config(
        default=config('DATABASE_URL')
    )
