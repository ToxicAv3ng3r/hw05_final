# Generated by Django 2.2.16 on 2022-04-05 15:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0008_post_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(help_text='Текст комментария', verbose_name='Комментарий')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Дата публикации комментария', verbose_name='Дата публикации комментария')),
                ('author', models.ForeignKey(help_text='Автор комментария', on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
                ('post', models.ForeignKey(blank=True, help_text='Комментарий к посту', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='posts.Post', verbose_name='Комментарий к посту')),
            ],
            options={
                'verbose_name': ('Комментарий',),
                'verbose_name_plural': 'Комментарии',
            },
        ),
    ]
