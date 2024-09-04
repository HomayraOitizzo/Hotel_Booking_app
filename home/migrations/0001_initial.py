# Generated by Django 5.0.1 on 2024-08-25 10:11

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Amenities',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('amenity_name', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('hotel_name', models.CharField(max_length=50)),
                ('hotel_price', models.IntegerField()),
                ('description', models.TextField()),
                ('room_count', models.IntegerField(default=10)),
                ('amenities', models.ManyToManyField(to='home.amenities')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HotelBooking',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('booking_type', models.CharField(choices=[('Pre Paid', 'Pre Paid'), ('Post Paid', 'Post Paid')], max_length=50)),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hotel_booking', to='home.hotel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_booking', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Hotelimages',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('images', models.ImageField(upload_to='hotels')),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hotel_images', to='home.hotel')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
