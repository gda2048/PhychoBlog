from django.shortcuts import render
from django.views.generic import ListView

from .models import Person, Achievement, Announcement, Article, HelpItem, Event


class PersonListView(ListView):
    model = Person
    template_name = 'people.html'
    context_object_name = 'authors_list'
    paginate_by = 1


class ArticleListView(ListView):
    model = Article
    template_name = 'articles.html'
    context_object_name = 'articles_list'
    paginate_by = 1


class AnnouncementListView(ListView):
    model = Announcement
    template_name = 'announcements.html'
    context_object_name = 'announcement_list'
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


class EventListView(ListView):
    model = Event
    template_name = 'events.html'
    context_object_name = 'event_list'
    paginate_by = 1

    def get_queryset(self):
        return Event.objects.filter(type=self.kwargs['type'])


def main(request):
    return render(request, 'main.html')


def shop(request):
    return render(request, 'shop.html')
