from django.db.models import Prefetch

from blog.models import Article, ArticlePhotoReport


def last_articles(num):
    last_article = Article.objects.order_by('-release_date')[:num] \
        .select_related('author').only("name", "id", "release_date", "author__id", "author__full_name", "content") \
        .prefetch_related(Prefetch("photos", to_attr="ph", queryset=ArticlePhotoReport.objects.filter(main=True)
                                   .only('photo', 'alt', 'id', 'height', "width", "article").distinct("article"))
                          )
    lst = list(next(iter(obj.ph), None) for obj in last_article)
    return list(zip(lst, list(last_article)))
