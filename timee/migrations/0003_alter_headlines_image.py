# Generated by Django 5.0 on 2023-12-04 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timee', '0002_headlines_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='headlines',
            name='image',
            field=models.URLField(blank=True, default=None, null=True),
        ),
    ]
