# Generated by Django 2.2.3 on 2019-07-30 12:12

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('events', '0009_auto_20190729_0851'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='duration',
        ),
    ]
