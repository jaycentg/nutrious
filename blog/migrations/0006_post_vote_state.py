# Generated by Django 4.1 on 2022-10-22 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='vote_state',
            field=models.IntegerField(default=2),
        ),
    ]
