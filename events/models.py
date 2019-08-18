from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone

from main.models import PhotoItem

EventType = (
    ('common', 'Обучение для всех'),
    ('prof', 'Обучение для профессионалов'),
    ('personal', 'Программы личностного роста'),
    ('university', 'Базовое психологическое образование'),
)


class Event(PhotoItem):
    """
    Stores information about a single event
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField("Название", max_length=100)
    content = models.TextField("Описание мероприятия", max_length=400, blank=True, null=True)
    start_date = models.DateTimeField('Дата и время начала мероприятия', null=True, blank=True)
    end_date = models.DateTimeField('Дата и время окончания мероприятия', null=True, blank=True)
    type = models.CharField('Тип', max_length=20, choices=EventType, default='common')

    def __str__(self):
        return self.name

    def clean(self):
        if self.end_date and self.end_date < self.start_date:
            raise ValidationError('Мероприятие не может закончиться раньше, чем начаться')

    def is_outdated(self):
        return 'Мероприятие прошло' if (self.start_date < timezone.now()) \
            else str((self.start_date - timezone.now()).days)

    def duration(self):
        if self.end_date and self.start_date:
            time = (self.end_date - self.start_date)
            if time.days > 0:
                return str(time.days) + ' дн.'
            elif time.seconds > 3600:
                return str(time.seconds // 3600) + ' ч.'

    is_outdated.short_description = 'Осталось дней'

    class Meta:

        """
        Event model settings
        """
        db_table = 'events'
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'
        ordering = ['-start_date']


class Announcement(models.Model):
    """
    Stores am announcement entry
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField("Название", max_length=100)
    content = models.TextField("Описание анонса", max_length=300, blank=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, verbose_name="Мероприятие", related_name='announcements')
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
