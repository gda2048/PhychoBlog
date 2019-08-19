from django.contrib import admin
from django.utils.html import mark_safe
from django_summernote.admin import get_attachment_model

admin.site.unregister(get_attachment_model())


class AdminImagePreviewMixin:
    readonly_fields = ['img_preview']

    def img_preview(self, obj):
        return mark_safe(
            '<img src="{url}" width="{width}" height={height} />'.format(url=obj.photo.url, width=obj.photo.width / 10,
                                                                         height=obj.photo.height / 10))

    img_preview.short_description = 'Предпросмотр фото'
