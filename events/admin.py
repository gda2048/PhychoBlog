from django.contrib import admin, messages
from django.db.models import Count
from django_summernote.admin import SummernoteModelAdmin, SummernoteInlineModelAdmin

from events.models import Event, Announcement
from main.admin import AdminImagePreviewMixin


class AnnouncementInline(admin.TabularInline, SummernoteInlineModelAdmin):
    summernote_fields = ('content',)
    model = Announcement
    fields = ['name', 'main', 'content']
    extra = 0
    classes = ['collapse']


@admin.register(Event)
class EventAdmin(AdminImagePreviewMixin, SummernoteModelAdmin):
    summernote_fields = ('content',)
    list_display = ('name', 'type', 'announcement_count', 'is_outdated')
    list_filter = ('type',)
    fields = ['name', ('start_date', 'end_date'), 'type', 'content',
              ('photo', AdminImagePreviewMixin.readonly_fields[0]), 'alt']
    inlines = [AnnouncementInline]
    list_per_page = 20
    date_hierarchy = 'start_date'

    def get_queryset(self, request):
        return super(EventAdmin, self).get_queryset(request).defer('binary_image', 'ext') \
            .annotate(announcements_count=Count('announcements', distinct=True))

    def save_model(self, request, obj, form, change):
        if obj.is_outdated():
            messages.add_message(request, messages.WARNING,
                                 'Вы работали с мероприятием, которое уже началось или прошло')
        super(EventAdmin, self).save_model(request, obj, form, change)

    def announcement_count(self, obj):
        return obj.announcements_count

    announcement_count.short_description = 'Количество анонсов'
