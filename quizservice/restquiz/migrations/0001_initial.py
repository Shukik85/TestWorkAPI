# Generated by Django 4.2.6 on 2023-10-22 22:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoryes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(unique=True, verbose_name='Категории')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(verbose_name='Вопрос')),
                ('question_id', models.IntegerField(unique=True, verbose_name='ID вопроса')),
                ('airdate', models.DateTimeField(verbose_name='Дата вопроса')),
                ('answer', models.CharField(verbose_name='Ответ')),
                ('value', models.IntegerField(blank=True, null=True, verbose_name='Очки')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restquiz.categoryes', to_field='title', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Вопрос',
                'verbose_name_plural': 'Вопросы',
                'ordering': ['category'],
            },
        ),
    ]
