"""
Stores all models of the project
"""
from django.db import models
from psycho.settings import MEDIA_ROOT


class Person(models.Model):
    """
    Stores all information about a psychologist
    """
    id = models.AutoField(primary_key=True)
    full_name = models.CharField('Полное имя', max_length=50)
    name = models.CharField('Имя', max_length=20, unique=True)
    birth_date = models.DateField('Дата рождения')
    email = models.EmailField()
    info = models.TextField('Основная информация', blank=True)
    bio = models.TextField('Биография', blank=True)
    photo = models.FilePathField('Фотография', path=MEDIA_ROOT, null=True, blank=True)
    password = models.CharField('Пароль', max_length=50)

    def __str__(self):
        return self.full_name

    class Meta:
        """
        Person model settings
        """
        db_table = 'people'
        verbose_name = 'Специалист'
        verbose_name_plural = 'Специалисты'


class Article(models.Model):
    """
    Stores a single article entry
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField("Название", max_length=50)
    content = models.TextField("Контент", blank=True)
    content_min = models.TextField("Миниверсия статьи", max_length=300, blank=True)
    release_date = models.DateField("Дата выпуска статьи", auto_now=True)
    author = models.ForeignKey(Person, on_delete=models.CASCADE, verbose_name='Автор')

    def __str__(self):
        return self.name

    class Meta:
        """
        Article model settings
        """
        db_table = 'articles'
        ordering = ['release_date']
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


class Announcement(models.Model):
    """
    Stores am announcement entry
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField("Название", max_length=50)
    content = models.TextField("Контент", max_length=200, blank=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name="Статья")
    date = models.DateField("Дата события")
    main = models.BooleanField("Отображать вверху", default=False)

    def __str__(self):
        return self.name

    class Meta:
        """
        Announcement model settings
        """
        db_table = 'announcements'
        ordering = ['date']
        verbose_name = 'Анонс'
        verbose_name_plural = 'Анонсы'


class HelpItem(models.Model):
    """
    Stores information about the type of help
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField("Название", max_length=50)
    description = models.CharField("Описание", max_length=200)
    expert = models.ForeignKey(Person, on_delete=models.CASCADE, verbose_name='Эксперт')

    class Meta:
        """
        HelpItem model settings
        """
        db_table = 'help'
        verbose_name = 'Пункт помощи'
        verbose_name_plural = 'Пункты помощи'


class PhotoItem(models.Model):
    """
    Abstract
    help to store information about the photo
    """
    id = models.AutoField(primary_key=True)
    alt = models.CharField("Описание", max_length=200, blank=True)
    height = models.PositiveIntegerField(null=True)
    width = models.PositiveIntegerField(null=True)
    photo = models.ImageField('Изображение', height_field='height', width_field='width', null=True)

    class Meta:
        """
        PhotoItem model settings
        """
        abstract = True
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинки'


class Achievement(PhotoItem):
    """
    Stores information about a single certificate or other proof of competence
    """
    priority = models.IntegerField("Приоритет", default=2)

    def __str__(self):
        return self.alt

    class Meta:
        """
        Achievement model settings
        """
        db_table = 'achievements'
        verbose_name = 'Достижение'
        verbose_name_plural = 'Достижения'


class ArticlePhotoReport(PhotoItem):
    """
    Stores photos for articles
    """
    article = models.ForeignKey(Article, on_delete=models.CASCADE, blank=True, verbose_name="Статья")
    announcement = models.BooleanField("Добавить в анонсы", default=False)

    class Meta:
        """
        ArticlePhotoReport model settings
        """
        db_table = 'photos'
        verbose_name = 'Фото для статьи'
        verbose_name_plural = 'Фото для статьи'
