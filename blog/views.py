from django.views.generic import ListView
from blog.models import Article


class ArticleListView(ListView):
    model = Article
    template_name = 'blog/articles.html'
    context_object_name = 'articles_list'
    paginate_by = 1
