from django.views.generic import ListView

from main.views import last_articles
from shop.models import Product


class ProductListView(ListView):
    model = Product
    template_name = 'shop/shop.html'
    context_object_name = 'product_list'

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context['last_articles'] = last_articles(1)
        return context
