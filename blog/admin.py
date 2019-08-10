from django.contrib import admin
from django.contrib import messages
from django.utils.html import mark_safe

from blog.models import Article, ArticlePhotoReport


class PictureInline(admin.TabularInline):
    model = ArticlePhotoReport
    extra = 0
    readonly_fields = ['img_preview']
    fields = ['article', 'photo', 'img_preview', 'alt', 'main']

    def img_preview(self, obj):
        return mark_safe(
            '<img src="{url}" width="{width}" height={height} />'.format(url=obj.photo.url, width=obj.photo.width / 10,
                                                                         height=obj.photo.height / 10))

    img_preview.short_description = 'Предпросмотр фото'


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('name', 'release_date', 'pictures_count', 'main_image')
    fields = ['name', 'author', 'content', 'content_min']
    inlines = [PictureInline]
    list_per_page = 20

    def main_image(self, obj):
        return obj.photos.filter(main=True)[:1].get()

    def pictures_count(self, obj):
        return obj.photos.count()

    pictures_count.short_description = 'Количество картинок'
    main_image.short_description = 'Изображение, которое будет показано'

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
        if not obj.author:
            obj.author = request.user.profile
        super().save_model(request, obj, *args)
        if len(obj.photos.filter(main=True)) > 1:
            messages.add_message(request, messages.WARNING, 'Вы выбрали несколько картинок для статьи для preview. '
                                                            'Лучше выбрать одну. ')
