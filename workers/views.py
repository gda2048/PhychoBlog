from django.views.generic import ListView
from workers.models import Person, Achievement, HelpItem


class PersonListView(ListView):
    model = Person
    template_name = 'people.html'
    context_object_name = 'authors_list'
    paginate_by = 1


class AchievementListView(ListView):
    model = Achievement
    template_name = 'achievements.html'
    context_object_name = 'achievement_list'
    paginate_by = 1


class HelpItemListView(ListView):
    model = HelpItem
    template_name = 'help_items.html'
    context_object_name = 'help_item_list'
    paginate_by = 1
