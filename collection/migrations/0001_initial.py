# Generated by Django 4.2.5 on 2023-09-15 10:52

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=225)),
                ('location', models.TextField()),
                ('horizon', models.TextField()),
                ('body', models.TextField()),
                ('date', models.DateField()),
                ('image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('slug', models.SlugField(unique=True)),
                ('collector', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, related_name='item_upload', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
