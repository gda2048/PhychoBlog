# Generated by Django 2.2.3 on 2019-07-26 10:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('workers', '0007_auto_20190726_1047'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='contacts',
            field=models.TextField('Биография', blank=True),
        ),
    ]
