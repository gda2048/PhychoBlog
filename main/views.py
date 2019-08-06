from django.shortcuts import render
from .models import Product
from django.views.generic import ListView
from blog.models import Article, ArticlePhotoReport
from django.db.models import Prefetch


def main(request):
    return render(request, 'main/main.html')


class ProductListView(ListView):
    model = Product
    template_name = 'main/shop.html'
    context_object_name = 'product_list'

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        last_articles = Article.objects.order_by('-release_date')[:1] \
            .select_related('author').only("name", "id", "release_date", "author__id", "author__full_name", "content") \
            .prefetch_related(Prefetch("photos", to_attr="ph", queryset=ArticlePhotoReport.objects.filter(main=True)
                                       .only('photo', 'alt', 'id', 'height', "width", "article").distinct("article"))
                              )
        lst = list(next(iter(obj.ph), None) for obj in last_articles)
        context['last_articles'] = list(zip(lst, list(last_articles)))
        return context
