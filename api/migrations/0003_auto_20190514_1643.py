# Generated by Django 2.0.5 on 2019-05-14 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_videos_videoid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videos',
            name='publishdatetime',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='videos',
            name='videoid',
            field=models.TextField(),
        ),
    ]
