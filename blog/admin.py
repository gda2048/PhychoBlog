from django.contrib import admin
from blog.models import Article, ArticlePhotoReport


@admin.register(ArticlePhotoReport)
class ArticlePhotoReportAdmin(admin.ModelAdmin):
    list_display = ('article', 'alt')
    fields = ['article', 'photo', 'alt']


class PictureInline(admin.TabularInline):
    model = ArticlePhotoReport
    exclude = ['width', 'height']
    extra = 0


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('name', 'release_date')
    fields = ['name', 'author', 'content', 'content_min']
    inlines = [PictureInline]

