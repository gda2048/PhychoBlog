from workers.views import *
from workers.models import Achievement, Person

import pytest


@pytest.mark.django_db
def test_binary_was_created():
    for obj in Achievement.objects.all():
        assert (obj.photo is None or obj.photo == '') == (obj.binary_image is None)
    for obj in Person.objects.all():
        assert (obj.photo is None or obj.photo == '') == (obj.binary_image is None)


@pytest.mark.django_db
def test_announcements_page(rf):
    request = rf.get('/author')
    response = PersonListView.as_view()(request)
    assert response.status_code == 200

