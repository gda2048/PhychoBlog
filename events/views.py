from django.views.generic import ListView, DetailView

from events.models import Event, Announcement
from blog.models import Article


class EventListView(ListView):
    model = Event
    template_name = 'events/events.html'
    context_object_name = 'event_list'
    paginate_by = 1

    def get_queryset(self):
        return Event.objects.filter(type=self.kwargs['type'])


class AnnouncementListView(ListView):
    model = Announcement
    template_name = 'events/announcements.html'
    context_object_name = 'announcement_list'
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super(AnnouncementListView, self).get_context_data(**kwargs)
        context['last_articles'] = Article.objects.order_by('-release_date')[:2]
        return context


class EventDetailView(DetailView):
    model = Event
    queryset = Event.objects.all()
    template_name = 'events/event.html'
