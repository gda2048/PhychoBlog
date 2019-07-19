from django.contrib import admin
from events.models import Event, Announcement


class EventAdmin(admin.ModelAdmin):
    exclude = ['width', 'height']
    list_display = ('name', 'type')
    list_filter = ('type',)


class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('name', 'event')


admin.site.register(Event, EventAdmin)
admin.site.register(Announcement, AnnouncementAdmin)

