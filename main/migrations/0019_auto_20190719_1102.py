# Generated by Django 2.2.3 on 2019-07-19 11:02

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('main', '0018_auto_20190719_1040'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articlephotoreport',
            name='article',
        ),
        migrations.DeleteModel(
            name='Article',
        ),
        migrations.DeleteModel(
            name='ArticlePhotoReport',
        ),
    ]
