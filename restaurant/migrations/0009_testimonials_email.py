# Generated by Django 5.1.7 on 2025-03-22 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0008_remove_testimonials_stars_testimonials_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='testimonials',
            name='email',
            field=models.EmailField(default='test@test.com', max_length=200),
        ),
    ]
