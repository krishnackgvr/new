# Generated by Django 4.1.6 on 2023-02-21 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='img',
            field=models.ImageField(default=2323, upload_to='gallery'),
            preserve_default=False,
        ),
    ]
