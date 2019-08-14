from django.views.generic import ListView, DetailView
from django.db.models import Prefetch

from workers.models import Person, Achievement, HelpItem
from blog.models import Article, ArticlePhotoReport


class PersonListView(ListView):
    queryset = Person.objects.defer("user_id", "binary_image", "birth_date", "ext")
    template_name = 'workers/people.html'
    context_object_name = 'authors_list'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(PersonListView, self).get_context_data(**kwargs)
        last_articles = Article.objects.order_by('-release_date')[:2] \
            .select_related('author').only("name", "id", "release_date", "author__id", "author__full_name", "content") \
            .prefetch_related(Prefetch("photos", to_attr="ph", queryset=ArticlePhotoReport.objects.filter(main=True)
                                       .only('photo', 'alt', 'id', 'height', "width", "article").distinct("article"))
                              )
        lst = list(next(iter(obj.ph), None) for obj in last_articles)
        context['last_articles'] = list(zip(lst, list(last_articles)))
        return context


class HelpItemListView(ListView):
    queryset = Person.objects.prefetch_related("help_items").defer('email', 'birth_date', 'binary_image', 'info', 'bio')
    template_name = 'workers/help_items.html'
    context_object_name = 'help_item_list'

    def get_context_data(self, **kwargs):
        context = super(HelpItemListView, self).get_context_data(**kwargs)
        last_articles = Article.objects.order_by('-release_date')[:2] \
            .select_related('author').only("name", "id", "release_date", "author__id", "author__full_name", "content") \
            .prefetch_related(Prefetch("photos", to_attr="ph", queryset=ArticlePhotoReport.objects.filter(main=True)
                                       .only('photo', 'alt', 'id', 'height', "width", "article").distinct("article"))
                              )
        lst = list(next(iter(obj.ph), None) for obj in last_articles)
        context['last_articles'] = list(zip(lst, list(last_articles)))
        return context


class PersonDetailView(DetailView):
    queryset = Person.objects.defer("user_id", "binary_image", "birth_date", "ext").prefetch_related(
        Prefetch("achievements",  queryset=Achievement.objects.defer('ext', "binary_image")))
    template_name = 'workers/worker.html'


class AchievementDetailView(DetailView):
    queryset = Achievement.objects.select_related("expert").only("id", 'photo', "alt", "height", "width", "expert__name")
    template_name = 'workers/achievement.html'
