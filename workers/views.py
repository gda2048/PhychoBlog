from django.views.generic import ListView, DetailView
from workers.models import Person, Achievement, HelpItem


class PersonListView(ListView):
    model = Person
    template_name = 'workers/people.html'
    context_object_name = 'authors_list'
    paginate_by = 1


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
