# Generated by Django 4.1 on 2022-10-27 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodsharing', '0002_rename_content_sharing_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='sharing',
            name='img',
            field=models.URLField(default='https://www.google.com/url?sa=i&url=https%3A%2F%2Fartsmidnorthcoast.com%2Flisting%2Fa-device-for-orienting-oneself-at-the-centre-of-the-universe%2Fno-image-available-icon-6%2F&psig=AOvVaw2-dCd7UtB_XHJmMsY7WB88&ust=1666987680917000&source=images&cd=vfe&ved=0CA0QjRxqFwoTCMj01ZabgfsCFQAAAAAdAAAAABAE'),
        ),
    ]
