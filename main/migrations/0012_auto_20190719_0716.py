# Generated by Django 2.2.3 on 2019-07-19 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20190719_0653'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articlephotoreport',
            name='announcement',
        ),
        migrations.AlterField(
            model_name='article',
            name='release_date',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата выпуска статьи'),
        ),
    ]