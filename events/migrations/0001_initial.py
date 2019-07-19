# Generated by Django 2.2.3 on 2019-07-19 10:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('photo', models.ImageField(blank=True, height_field='height', null=True, upload_to='', verbose_name='Изображение', width_field='width')),
                ('alt', models.TextField(blank=True, max_length=200, verbose_name='Описание фото')),
                ('height', models.PositiveIntegerField(blank=True, null=True)),
                ('width', models.PositiveIntegerField(blank=True, null=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('content', models.TextField(blank=True, max_length=200, null=True, verbose_name='Контент')),
                ('start_date', models.DateTimeField(verbose_name='Дата начала мероприятия')),
                ('duration', models.CharField(blank=True, max_length=20, null=True, verbose_name='Длительность')),
                ('type', models.CharField(choices=[('common', 'Обучение для всех'), ('prof', 'Обучение для профессионалов'), ('personal', 'Программы личностного роста'), ('university', 'Базовое психологическое образование в хгак')], default='common', max_length=20)),
            ],
            options={
                'verbose_name': 'Мероприятие',
                'verbose_name_plural': 'Мероприятия',
                'db_table': 'events',
            },
        ),
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('content', models.TextField(blank=True, max_length=200, verbose_name='Контент')),
                ('main', models.BooleanField(default=False, verbose_name='Отображать вверху')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Event', verbose_name='Мероприятие')),
            ],
            options={
                'verbose_name': 'Анонс',
                'verbose_name_plural': 'Анонсы',
                'db_table': 'announcements',
                'ordering': ['-main', 'event__start_date'],
            },
        ),
    ]
