# Generated by Django 2.2.3 on 2019-07-25 09:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('blog', '0007_articlephotoreport_main'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlephotoreport',
            name='alt',
            field=models.TextField(blank=True, max_length=200, null=True, verbose_name='Описание фото'),
        ),
    ]
