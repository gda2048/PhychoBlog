from django.db.models import Prefetch
from django.views.generic import ListView, DetailView

from main.views import last_articles
from workers.models import Person, Achievement


class PersonListView(ListView):
    queryset = Person.objects.defer("user_id", "binary_image", "birth_date", "ext")
    template_name = 'workers/people.html'
    context_object_name = 'authors_list'
    paginate_by = 8

    def get_context_data(self, **kwargs):
        context = super(PersonListView, self).get_context_data(**kwargs)
        context['last_articles'] = last_articles(2)
        return context


class HelpItemListView(ListView):
    queryset = Person.objects.prefetch_related("help_items").defer('email', 'birth_date', 'binary_image', 'info', 'bio')
    template_name = 'workers/help_items.html'
    context_object_name = 'help_item_list'

    def get_context_data(self, **kwargs):
        context = super(HelpItemListView, self).get_context_data(**kwargs)
        context['last_articles'] = last_articles(2)
        return context


class PersonDetailView(DetailView):
    queryset = Person.objects.defer("user_id", "binary_image", "birth_date", "ext").prefetch_related(
        Prefetch("achievements",  queryset=Achievement.objects.defer('ext', "binary_image")))
    template_name = 'workers/worker.html'


class AchievementDetailView(DetailView):
    queryset = Achievement.objects.select_related("expert").only("id", 'photo', "alt", "height", "width", "expert__name")
    template_name = 'workers/achievement.html'
