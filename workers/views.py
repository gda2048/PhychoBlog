from django.views.generic import ListView, DetailView

from workers.models import Person, Achievement, HelpItem
from blog.models import Article


class PersonListView(ListView):
    model = Person
    template_name = 'workers/people.html'
    context_object_name = 'authors_list'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(PersonListView, self).get_context_data(**kwargs)
        context['last_articles'] = Article.objects.order_by('-release_date')[:3]
        return context


class AchievementListView(ListView):
    model = Achievement
    template_name = 'workers/achievements.html'
    context_object_name = 'achievement_list'
    paginate_by = 1


class HelpItemListView(ListView):
    model = HelpItem
    template_name = 'workers/help_items.html'
    context_object_name = 'help_item_list'
    paginate_by = 1


class PersonDetailView(DetailView):
    model = Person
    queryset = Person.objects.all()
    template_name = 'workers/worker.html'


class AchievementDetailView(DetailView):
    model = Achievement
    queryset = Achievement.objects.all()
    template_name = 'workers/achievement.html'
