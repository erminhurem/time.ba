# Generated by Django 5.0 on 2024-01-11 18:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timee', '0020_rename_lastfetchtime_lastfetch'),
    ]

    operations = [
        migrations.DeleteModel(
            name='LastFetch',
        ),
    ]
