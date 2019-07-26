from django.views.generic import ListView, DetailView

from blog.models import Article


class ArticleListView(ListView):
    model = Article
    template_name = 'blog/articles.html'
    context_object_name = 'articles_list'
    paginate_by = 6


class ArticleDetailView(DetailView):
    model = Article
    success_url = '/article/'
    template_name = 'blog/article.html'

    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        context['images'] = Article.objects.get(pk=self.kwargs['pk']).photos.exclude(binary_image=None)
        context['last_articles'] = Article.objects.order_by('-release_date').exclude(id__in=[self.object.id])[:2]
        return context
