# Generated by Django 4.0.5 on 2022-06-12 11:18

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('feed', '0003_tweet_likes'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='tweet',
            new_name='post',
        ),
    ]