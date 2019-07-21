from django.views.generic import ListView
from events.models import Event, Announcement


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
    paginate_by = 1
