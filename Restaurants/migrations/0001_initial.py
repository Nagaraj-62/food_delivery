# Generated by Django 5.1.2 on 2024-12-15 16:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('cat_id', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('images', models.ImageField(upload_to='category')),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Restaurant_name', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('phone_number', models.CharField(max_length=15)),
                ('opening_time', models.TimeField()),
                ('closing_time', models.TimeField()),
                ('logo', models.ImageField(blank=True, null=True, upload_to='restaurant_logos/')),
                ('rating', models.FloatField(default=0.0)),
                ('total_reviews', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='FoodItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('is_available', models.BooleanField(default=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='food_images/')),
                ('category_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Restaurants.category')),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Restaurants.restaurant')),
            ],
        ),
    ]
