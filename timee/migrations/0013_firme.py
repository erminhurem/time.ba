# Generated by Django 5.0 on 2024-01-10 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timee', '0012_lastfetchtime'),
    ]

    operations = [
        migrations.CreateModel(
            name='Firme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_broj', models.IntegerField(default=None, max_length=50)),
                ('naziv_kompanije', models.CharField(default=None, max_length=100)),
                ('adresa', models.CharField(default=None, max_length=50)),
                ('sifra', models.IntegerField(default=None, max_length=50)),
                ('opstina', models.CharField(default=None, max_length=50)),
            ],
        ),
    ]
