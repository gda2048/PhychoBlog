"""
Stores main models of the project
"""
from django.db import models


class PhotoItem(models.Model):
    """
    Abstract
    help to store information about the photo
    """
    id = models.AutoField(primary_key=True)
    photo = models.ImageField('Изображение', height_field='height', width_field='width', null=True, blank=True)
    alt = models.TextField("Описание фото", max_length=200, blank=True)
    height = models.PositiveIntegerField(null=True, blank=True)
    width = models.PositiveIntegerField(null=True, blank=True)

    class Meta:
        """
        PhotoItem model settings
        """
        abstract = True
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинки'

