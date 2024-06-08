# Generated by Django 5.0.6 on 2024-06-05 17:50

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=20),
        ),
        migrations.AlterField(
            model_name='story',
            name='image',
            field=cloudinary.models.CloudinaryField(default='', max_length=255, verbose_name='image'),
            preserve_default=False,
        ),
    ]