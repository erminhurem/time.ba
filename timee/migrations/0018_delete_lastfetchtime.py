# Generated by Django 5.0 on 2024-01-11 18:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timee', '0017_remove_lastfetchtime_update_time_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='LastFetchTime',
        ),
    ]
