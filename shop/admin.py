from django.contrib import admin

from main.admin import AdminImagePreviewMixin
from .models import Product


@admin.register(Product)
class ProductAdmin(AdminImagePreviewMixin, admin.ModelAdmin):
    fields = ['name', 'about', ('author', 'description'), 'contacts', 'price', ('photo', 'img_preview'), 'alt']

    def get_queryset(self, request):
        return super(ProductAdmin, self).get_queryset(request).defer('ext', 'binary_image')
