# Generated by Django 4.1 on 2022-10-28 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("recipe", "0002_foodrecipe_author_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="foodrecipe",
            name="formatted_date",
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
