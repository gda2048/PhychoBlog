from django.contrib import admin
from events.models import Event, Announcement
from django.utils.html import mark_safe


class AnnouncementInline(admin.TabularInline):
    model = Announcement
    fields = ['name', 'main', 'content']
    extra = 0


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    exclude = ['width', 'height']
    list_display = ('name', 'type')
    list_filter = ('type',)
    fields = ['name', ('start_date', 'duration'), 'type', 'content', ('photo', 'img_preview'), 'alt']
    inlines = [AnnouncementInline]
    readonly_fields = ['img_preview']

    def img_preview(self, obj):
        return mark_safe(
            '<img src="{url}" width="{width}" height={height} />'.format(url=obj.photo.url, width=obj.photo.width/10,
                                                                         height=obj.photo.height/10))

    img_preview.short_description = 'Предпросмотр фото'

