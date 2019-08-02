from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Prefetch

from blog.models import Article, ArticlePhotoReport


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

    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        context['images'] = Article.objects.get(pk=self.kwargs['pk']).photos.exclude(binary_image=None)
        context['last_articles'] = Article.objects.order_by('-release_date').exclude(id__in=[self.object.id])[:2]
        return context
