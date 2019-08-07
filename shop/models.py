from django.db import models
from main.models import PhotoItem


class Product(PhotoItem):
    name = models.CharField("Название", max_length=100)
    about = models.TextField('Краткое описание', max_length=500)
    author = models.TextField('Про автора', max_length=500)
    description = models.TextField('Полное описание', blank=True)
    contacts = models.TextField('Другие контактные данные: ', blank=True)
    price = models.DecimalField('Цена', max_digits=8, decimal_places=2, null=True, default=0, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        """
        Product model settings
        """
        db_table = 'products'
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
