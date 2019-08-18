from django.contrib import admin
from django.contrib import messages
from django.db.models import Prefetch, Count, Subquery, OuterRef

from blog.models import Article, ArticlePhotoReport
from main.admin import AdminImagePreviewMixin


class PictureInline(AdminImagePreviewMixin, admin.TabularInline):
    model = ArticlePhotoReport
    extra = 0
    fields = ['article', 'photo', 'alt', 'main'] + AdminImagePreviewMixin.readonly_fields
    classes = ['collapse']

    def get_queryset(self, request):
        return super(PictureInline, self).get_queryset(request).defer('binary_image', 'ext')


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('name', 'release_date', 'pictures_count', 'main_image')
    fields = ['name', 'author', ('content', 'content_min')]
    inlines = [PictureInline]
    list_per_page = 20

    def main_image(self, obj):
        return obj.main_photo

    def pictures_count(self, obj):
        return obj.photos_count

    main_image.short_description = 'Изображение, которое будет показано'
    pictures_count.short_description = 'Количество картинок'

    def get_readonly_fields(self, request, obj=None):
        if request.user.is_staff:
            if request.user.is_superuser:
                return []
            else:
                return ['author']

    def get_queryset(self, request):
        qs = super(ArticleAdmin, self).get_queryset(request) \
            .prefetch_related(Prefetch("photos", queryset=ArticlePhotoReport.objects.defer('binary_image', 'ext'))). \
            annotate(
            photos_count=Count("photos", distinct=True),
            main_photo=Subquery(
                ArticlePhotoReport.objects.filter(article=OuterRef('pk'), main=True).values_list('alt')[:1]
            )
        )
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
