from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Prefetch
from django.views.generic import ListView, DetailView

from blog.models import Article, ArticlePhotoReport
from main.views import last_articles


class ArticleListView(ListView):
    queryset = Article.objects.only(
        'id', 'name', 'release_date', 'content', 'content_min', 'author__id', 'author__full_name'
    ).select_related(
        "author"
    ).prefetch_related(
        Prefetch("photos", to_attr='ph', queryset=ArticlePhotoReport.objects.filter(main=True)
                 .only('photo', 'alt', 'id', 'height', "width", "article_id").distinct("article"))
    )

    template_name = 'blog/articles.html'
    paginate_by = 6

    def get_context_data(self, *args, **kwargs):
        context = super(self.__class__, self).get_context_data(*args, **kwargs)

        lst = list(next(iter(obj.ph), None) for obj in self.object_list)
        articles = list(zip(lst, list(self.object_list)))

        paginator = Paginator(articles, self.paginate_by)
        page = self.request.GET.get('page')
        try:
            articles = paginator.page(page)
        except PageNotAnInteger:
            articles = paginator.page(1)
        except EmptyPage:
            articles = paginator.page(paginator.num_pages)
        context["articles"] = articles
        return context


class ArticleDetailView(DetailView):
    model = Article
    success_url = '/article/'
    template_name = 'blog/article.html'
    queryset = Article.objects.select_related('author') \
        .only("author__full_name", "author__id", "name", "id", "release_date", "content").prefetch_related(
        Prefetch("photos", to_attr="images",
                 queryset=ArticlePhotoReport.objects.exclude(ext=None).defer('binary_image'))
    )

    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        context['last_articles'] = last_articles(2, self.object.id)
        return context
