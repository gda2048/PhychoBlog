from django.contrib.auth.models import User
from django.db import models

from main.models import PhotoItem
from psycho.settings import st_password


class Person(PhotoItem):
    """
    Stores all information about a psychologist
    """
    id = models.AutoField(primary_key=True)
    full_name = models.CharField('Имя', max_length=50)
    name = models.CharField('Логин', max_length=20, unique=True,
                            help_text='Уникальный логин. При входе в систему его нужно будет указывать. ')
    birth_date = models.DateField('Дата рождения')
    email = models.EmailField()
    info = models.TextField('Основная информация', blank=True,
                            help_text='Хорошее краткое описание своей деятельности')
    bio = models.TextField('Биография', blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.user:
            user = User.objects.get(id=self.user.id)
            user.username, user.email = self.name, self.email
            user.save()
        else:
            user = User.objects.create_user(self.name, self.email, st_password)
            user.save()
            self.user = user
            user.groups.add(1)
            user.is_staff = True
            user.save()
        self.save_photo()
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        user = User.objects.get(id=self.user.id)
        if not user.is_superuser:
            user.delete()
            super().delete(*args, **kwargs)

    def __str__(self):
        return self.full_name

    class Meta:
        """
        Person model settings
        """
        db_table = 'people'
        verbose_name = 'Специалист'
        verbose_name_plural = 'Специалисты'
        ordering = ['-user__is_superuser']


class HelpItem(models.Model):
    """
    Stores information about the type of help
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField("Название", max_length=50, help_text='С чем работает эксперт?')
    description = models.TextField("Описание", null=True, blank=True, max_length=200)
    expert = models.ForeignKey(Person, on_delete=models.CASCADE, verbose_name='Эксперт', related_name='help_items')

    def __str__(self):
        return self.name

    class Meta:
        """
        HelpItem model settings
        """
        ordering = ['-id']
        db_table = 'help'
        verbose_name = 'Пункт помощи'
        verbose_name_plural = 'Пункты помощи'


class Achievement(PhotoItem):
    """
    Stores information about a single certificate or other proof of competence
    """
    priority = models.IntegerField("Приоритет", default=2,
                                   help_text='Чем больше приоритет, тем выше в списке будет достижение')
    expert = models.ForeignKey(Person, on_delete=models.CASCADE, verbose_name='Эксперт', related_name='achievements')

    def __str__(self):
        return self.alt

    class Meta:
        """
        Achievement model settings
        """
        db_table = 'achievements'
        verbose_name = 'Достижение'
        ordering = ['-priority']
        verbose_name_plural = 'Достижения'
