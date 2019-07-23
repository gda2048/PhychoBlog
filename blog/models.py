from django.db import models
from main.models import PhotoItem
from workers.models import Person


class Article(models.Model):
    """
    Stores a single article entry
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField("Название", max_length=50)
    content = models.TextField("Содержание", blank=True)
    content_min = models.TextField("Миниверсия статьи", max_length=300, blank=True,
                                   help_text='Как статья отображается в свернутом виде. Максимум 200 символов.')
    release_date = models.DateTimeField("Дата выпуска статьи", auto_now_add=True)
    author = models.ForeignKey(Person, on_delete=models.CASCADE, verbose_name='Автор', related_name='author',
                               null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        """
        Article model settings
        """
        db_table = 'articles'
        ordering = ['-release_date']
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


class ArticlePhotoReport(PhotoItem):
    """
    Stores photos for articles
    """
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name="Статья", related_name='photos',
                                help_text='К какой статье относится картинка')

    def __str__(self):
        return self.alt

    class Meta:
        """
        ArticlePhotoReport model settings
        """
        db_table = 'photos'
        verbose_name = 'Фото для статей'
        verbose_name_plural = 'Фото для статей'
