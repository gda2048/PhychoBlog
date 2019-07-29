from django.contrib import admin
from django.utils.html import mark_safe

from events.models import Event, Announcement


class AnnouncementInline(admin.TabularInline):
    model = Announcement
    fields = ['name', 'main', 'content']
    extra = 0


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    exclude = ['width', 'height']
    list_display = ('name', 'type', 'announcement_count', 'is_outdated')
    list_filter = ('type',)
    fields = ['name', ('start_date', 'end_date'), 'type', 'content', ('photo', 'img_preview'), 'alt']
    inlines = [AnnouncementInline]
    readonly_fields = ['img_preview']
    list_per_page = 20
    date_hierarchy = 'start_date'

    def announcement_count(self, obj):
        return obj.announcements.count()

    announcement_count.short_description = 'Количество анонсов'

    def img_preview(self, obj):
        return mark_safe(
            '<img src="{url}" width="{width}" height={height} />'.format(url=obj.photo.url, width=obj.photo.width / 10,
                                                                         height=obj.photo.height / 10))

    img_preview.short_description = 'Предпросмотр фото'
