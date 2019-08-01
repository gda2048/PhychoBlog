from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from blog.models import Article, ArticlePhotoReport


class ArticleListView(ListView):
    queryset = Article.objects.select_related("author").prefetch_related("photos").filter(photos__main=True)
    template_name = 'blog/articles.html'
    context_object_name = 'articles_list'
    paginate_by = 6

    def get_context_data(self, *args, **kwargs):
        photos = []
        for obj in self.object_list:
            photos += obj.photos.all()

        photo_dict = {obj.article: obj for obj in photos}
        lst = [photo_dict.get(obj) for obj in self.object_list]
        articles = list(zip(lst, list(self.object_list)))

        paginator = Paginator(articles, self.paginate_by)
        page = self.request.GET.get('page')
        try:
            articles = paginator.page(page)
        except PageNotAnInteger:
            articles = paginator.page(1)
        except EmptyPage:
            articles = paginator.page(paginator.num_pages)
        context = {"articles": articles}
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
