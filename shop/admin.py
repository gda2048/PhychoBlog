from django.contrib import admin

from django_summernote.admin import SummernoteModelAdmin
from main.admin import AdminImagePreviewMixin
from .models import Product


@admin.register(Product)
class ProductAdmin(AdminImagePreviewMixin, SummernoteModelAdmin):
    summernote_fields = ('about', 'author', 'description', 'contacts')
    fields = ['name', 'about', ('author', 'description'), 'contacts', 'price', ('photo', 'img_preview'), 'alt']

    def get_queryset(self, request):
            return super(ProductAdmin, self).get_queryset(request).defer('ext', 'binary_image')
