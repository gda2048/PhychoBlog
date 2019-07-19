from django.contrib import admin
from events.models import Event, Announcement


class EventAdmin(admin.ModelAdmin):
    exclude = ['width', 'height']
    list_display = ('name', 'type')
    list_filter = ('type',)
    fields = ['name', ('start_date', 'duration'), 'type', 'content', 'photo', 'alt']


class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('name', 'event')
    fields = ['name', ('event', 'main'), 'content']


admin.site.register(Event, EventAdmin)
admin.site.register(Announcement, AnnouncementAdmin)

