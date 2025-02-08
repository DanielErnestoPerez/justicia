# Generated by Django 5.1.5 on 2025-02-08 04:32

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('justicia_app', '0004_post_image_alter_post_imagen_fondo_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
        migrations.AlterField(
            model_name='post',
            name='imagen_fondo',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='post',
            name='imagen_portada',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='image'),
        ),
    ]
