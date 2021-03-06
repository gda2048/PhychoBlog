# Generated by Django 2.2.4 on 2019-08-06 08:56

from django.db import migrations, models

import main.models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('main', '0020_auto_20190719_1139'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('photo', models.ImageField(blank=True, height_field='height', null=True, upload_to='',
                                            validators=[main.models.validate_name], verbose_name='Изображение',
                                            width_field='width')),
                ('alt', models.TextField(blank=True, max_length=200, null=True, verbose_name='Описание фото')),
                ('height', models.PositiveIntegerField(blank=True, null=True)),
                ('width', models.PositiveIntegerField(blank=True, null=True)),
                ('binary_image', models.BinaryField(null=True)),
                ('ext', models.CharField(blank=True, max_length=10, null=True)),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('about', models.CharField(blank=True, max_length=300, verbose_name='Краткое описание')),
                ('author', models.CharField(blank=True, max_length=300, verbose_name='Краткое описание')),
                ('description', models.TextField(blank=True, verbose_name='Краткое описание')),
                ('contacts', models.TextField(blank=True, verbose_name='Другие контактные данные: ')),
                ('Price', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
                'db_table': 'products',
            },
        ),
    ]
