# Generated by Django 5.0.1 on 2024-02-02 06:50

import cloudinary.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=50, verbose_name='Name')),
                ('description', models.CharField(db_index=True, max_length=500, verbose_name='Description')),
                ('time_to_travel', models.CharField(max_length=20, verbose_name='Time_to_travel')),
                ('google_map_link', models.CharField(max_length=500, verbose_name='Google_map_link')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='updated_at')),
                ('image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('place_type', models.CharField(choices=[('Private and Luxury', 'Private and Luxury'), ('Full-day Tours', 'Full-day Tours'), ('Day trips', 'Day trips'), ('Forest', 'Forest'), ('Favorites', 'Favorites')], max_length=50, verbose_name='Place Type')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categories.category')),
            ],
            options={
                'db_table': 'place',
            },
        ),
    ]