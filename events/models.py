from django.db import models
from main.models import PhotoItem

EventType = (
    ('common', 'Обучение для всех'),
    ('prof', 'Обучение для профессионалов'),
    ('personal', 'Программы личностного роста'),
    ('university', 'Базовое психологическое образование в хгак'),
)


class Event(PhotoItem):
    """
    Stores information about a single event
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField("Название", max_length=50)
    content = models.TextField("Контент", max_length=200, blank=True, null=True)
    start_date = models.DateTimeField('Дата начала мероприятия')
    duration = models.CharField('Длительность', max_length=20, blank=True, null=True)
    type = models.CharField('Тип', max_length=20, choices=EventType, default='common')

    def __str__(self):
        return self.name

    class Meta:
        """
        Event model settings
        """
        db_table = 'events'
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'


class Announcement(models.Model):
    """
    Stores am announcement entry
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField("Название", max_length=50)
    content = models.TextField("Контент", max_length=200, blank=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, verbose_name="Мероприятие")
    main = models.BooleanField("Отображать вверху", default=False)

    def __str__(self):
        return self.name

    class Meta:
        """
        Announcement model settings
        """
        db_table = 'announcements'
        ordering = ['-main', 'event__start_date']
        verbose_name = 'Анонс'
        verbose_name_plural = 'Анонсы'
