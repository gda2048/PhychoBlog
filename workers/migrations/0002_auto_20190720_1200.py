# Generated by Django 2.2.3 on 2019-07-20 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='achievement',
            name='priority',
            field=models.IntegerField(default=2, help_text='Чем больше приоритет, тем выше в списке будет достижение', verbose_name='Приоритет'),
        ),
        migrations.AlterField(
            model_name='helpitem',
            name='name',
            field=models.CharField(help_text='С чем работает эксперт?', max_length=50, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='person',
            name='full_name',
            field=models.CharField(max_length=50, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='person',
            name='info',
            field=models.TextField(blank=True, help_text='Хорошее краткое описание своей деятельности', verbose_name='Основная информация'),
        ),
        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.CharField(help_text='Уникальный логин. При входе в систему его нужно будет указывать. ', max_length=20, unique=True, verbose_name='Логин'),
        ),
    ]
