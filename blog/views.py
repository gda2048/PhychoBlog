from django.views.generic import ListView, DetailView

from blog.models import Article


class ArticleListView(ListView):
    model = Article
    template_name = 'blog/articles.html'
    context_object_name = 'articles_list'
    paginate_by = 1


class ArticleDetailView(DetailView):
    model = Article
    queryset = Article.objects.all()
    success_url = '/article/'
    template_name = 'blog/article.html'
