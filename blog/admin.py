from django.contrib import admin
from blog.models import Article, ArticlePhotoReport


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('name', 'release_date')


class ArticlePhotoReportAdmin(admin.ModelAdmin):
    exclude = ['width', 'height']
    list_display = ('article',)


admin.site.register(Article, ArticleAdmin)
admin.site.register(ArticlePhotoReport, ArticlePhotoReportAdmin)
