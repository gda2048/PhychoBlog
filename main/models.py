"""
Stores main models of the project
"""
from django.core.exceptions import ValidationError
from django.db import models
from PIL import Image
from io import BytesIO


def validate_name(value):
    print(value.name)
    if not all([letter.isalpha() or letter.isdigit() or letter in ['_', '.'] for letter in value.name]):
        raise ValidationError('Измените название картинки и загрузите ее снова. Присутствуют неподдерживаемые символы')


class PhotoItem(models.Model):
    """
    Abstract
    help to store information about the photo
    """
    id = models.AutoField(primary_key=True)
    photo = models.ImageField('Изображение', height_field='height', width_field='width', null=True, blank=True,
                              validators=[validate_name])
    alt = models.TextField("Описание фото", max_length=200, blank=True, null=True)
    height = models.PositiveIntegerField(null=True, blank=True)
    width = models.PositiveIntegerField(null=True, blank=True)
    binary_image = models.BinaryField(null=True)
    ext = models.CharField(max_length=10, null=True, blank=True)

    def save_photo(self):
        if self.photo:
            self.photo.open()
            with BytesIO() as output:
                with Image.open(self.photo) as img:
                    self.ext = img.format
                    img.save(output, self.ext)
                self.binary_image = output.getvalue()

            if self.alt == '':
                self.alt = self.photo.name
        else:
            self.binary_image = None

    def save(self, *args, **kwargs):
        self.save_photo()
        super(PhotoItem, self).save(*args, **kwargs)

    def img_from_binary(self):
        if self.photo and self.binary_image:
            try:
                self.photo.open()
            except FileNotFoundError:
                Image.open(BytesIO(self.binary_image)).save(self.photo.path)

    @classmethod
    def all_img_from_binary(cls):
        for obj in cls.objects.all():
            obj.img_from_binary()

    class Meta:
        """
        PhotoItem model settings
        """
        abstract = True
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинки'
