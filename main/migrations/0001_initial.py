# Generated by Django 3.2.8 on 2021-10-27 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='ФИО клиента')),
                ('country', models.CharField(max_length=100, verbose_name='Город проживание')),
                ('image', models.ImageField(upload_to='images/', verbose_name='Изображение')),
                ('text', models.TextField(verbose_name='Отзыв')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
        migrations.CreateModel(
            name='Slaider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Заголовок')),
                ('sub_title', models.CharField(max_length=50, verbose_name='Подзаголовок')),
                ('image', models.ImageField(upload_to='images/', verbose_name='Изображение')),
                ('button_name', models.CharField(max_length=20, verbose_name='Название кнопки')),
                ('button_url', models.URLField(verbose_name='URL для кнопки')),
            ],
            options={
                'verbose_name': 'Новость в слайдере',
                'verbose_name_plural': 'Новости в слайдере',
            },
        ),
    ]