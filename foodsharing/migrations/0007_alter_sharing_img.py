# Generated by Django 4.1 on 2022-10-28 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodsharing', '0006_alter_sharing_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sharing',
            name='img',
            field=models.TextField(),
        ),
    ]
