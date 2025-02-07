# Generated by Django 5.1.5 on 2025-02-07 13:46

import django_resized.forms
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, null=True, quality=90, scale=None, size=[600, 600], upload_to='profiles'),
        ),
    ]
