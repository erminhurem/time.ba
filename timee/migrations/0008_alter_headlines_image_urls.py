# Generated by Django 5.0 on 2023-12-14 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timee', '0007_alter_headlines_image_urls'),
    ]

    operations = [
        migrations.AlterField(
            model_name='headlines',
            name='image_urls',
            field=models.URLField(blank=True, default=None, max_length=1000, null=True),
        ),
    ]
