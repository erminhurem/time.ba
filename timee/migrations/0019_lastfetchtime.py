# Generated by Django 5.0 on 2024-01-11 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timee', '0018_delete_lastfetchtime'),
    ]

    operations = [
        migrations.CreateModel(
            name='LastFetchTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_update_time', models.DateTimeField(default=None)),
            ],
        ),
    ]
