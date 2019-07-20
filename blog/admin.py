from django.contrib import admin
from django.utils.html import mark_safe

from blog.models import Article, ArticlePhotoReport


class PictureInline(admin.TabularInline):
    model = ArticlePhotoReport
    extra = 0
    readonly_fields = ['img_preview']
    fields = ['article', 'photo', 'img_preview', 'alt']

    def img_preview(self, obj):
        return mark_safe(
            '<img src="{url}" width="{width}" height={height} />'.format(url=obj.photo.url, width=obj.photo.width/10,
                                                                         height=obj.photo.height/10))

    img_preview.short_description = 'Предпросмотр фото'


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('name', 'release_date')
    fields = ['name', 'author', 'content', 'content_min']
    inlines = [PictureInline]

    def get_readonly_fields(self, request, obj=None):
        if request.user.is_staff:
            if request.user.is_superuser:
                return []
            else:
                return ['author']

    def get_queryset(self, request):
        qs = super(ArticleAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        else:
            return qs.filter(author=request.user.profile)

    def save_model(self, request, obj, *args):
        obj.author = request.user.profile
        super().save_model(request, obj, *args)
