from django.contrib import admin
from .models import Product
from django.utils.html import mark_safe


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    exclude = ['width', 'height']
    readonly_fields = ['img_preview']
    fields = ['name', 'about', 'author', 'description', 'contacts', 'price', ('photo', 'img_preview'), 'alt']

    def img_preview(self, obj):
        return mark_safe(
            '<img src="{url}" width="{width}" height={height} />'.format(url=obj.photo.url, width=obj.photo.width / 10,
                                                                         height=obj.photo.height / 10))

    img_preview.short_description = 'Предпросмотр фото'
