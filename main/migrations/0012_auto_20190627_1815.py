# Generated by Django 2.1.7 on 2019-06-27 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20190627_1751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='achievement',
            name='photo',
            field=models.ImageField(height_field='ach_h', null=True, upload_to='article/', verbose_name='Изображение', width_field='ach_w'),
        ),
        migrations.AlterField(
            model_name='articlephotoreport',
            name='photo',
            field=models.ImageField(height_field='ach_h', null=True, upload_to='article/', verbose_name='Изображение', width_field='ach_w'),
        ),
    ]
