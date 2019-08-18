from django.views.generic import ListView, DetailView

from events.models import Event, Announcement
from main.views import last_articles


class EventListView(ListView):
    model = Event
    template_name = 'events/events.html'
    context_object_name = 'event_list'
    paginate_by = 6

    def get_queryset(self):
        return Event.objects.filter(type=self.kwargs['type']).defer("binary_image", "ext")


class AnnouncementListView(ListView):
    queryset = Announcement.objects.select_related("event") \
        .only("id", "content", "event__id", "name",
              "event__alt", "event__width", "event__height", 'event__photo', "event__end_date", "event__start_date")
    template_name = 'events/announcements.html'
    context_object_name = 'announcement_list'
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super(AnnouncementListView, self).get_context_data(**kwargs)
        context['last_articles'] = last_articles(2)
        return context


class EventDetailView(DetailView):
    model = Event
    queryset = Event.objects.all()
    template_name = 'events/event.html'
