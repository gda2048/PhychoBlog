# Generated by Django 2.2.3 on 2019-07-17 08:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20190717_0829'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='announcement',
            options={'ordering': ['-main', 'event__start_date'], 'verbose_name': 'Анонс', 'verbose_name_plural': 'Анонсы'},
        ),
    ]