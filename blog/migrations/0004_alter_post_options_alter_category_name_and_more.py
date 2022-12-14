# Generated by Django 4.0.5 on 2022-08-18 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_category_post_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['title'], 'verbose_name': 'Пост', 'verbose_name_plural': 'Посты'},
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(blank=True, db_index=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='comments',
            name='status',
            field=models.BooleanField(default=True, verbose_name='Видимость статьи'),
        ),
        migrations.RemoveField(
            model_name='post',
            name='category',
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ManyToManyField(related_name='posts', to='blog.category'),
        ),
    ]
