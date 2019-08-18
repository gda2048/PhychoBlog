import pytest

from blog.views import *


@pytest.mark.django_db
def test_binary_was_created():
    for obj in ArticlePhotoReport.objects.all():
        assert (obj.photo is None or obj.photo == '') == (obj.binary_image is None)


@pytest.mark.django_db
def test_announcements_page(rf):
    request = rf.get('/article')
    response = ArticleListView.as_view()(request)
    assert response.status_code == 200
