# Generated by Django 4.1 on 2022-10-20 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_post_status_remove_post_updated_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='downvote',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='upvote',
            field=models.IntegerField(default=0),
        ),
    ]
