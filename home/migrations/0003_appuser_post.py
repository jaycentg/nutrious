# Generated by Django 4.1 on 2022-10-21 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_remove_post_author_alter_post_title'),
        ('home', '0002_alter_appuser_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='appuser',
            name='post',
            field=models.ManyToManyField(to='blog.post'),
        ),
    ]
