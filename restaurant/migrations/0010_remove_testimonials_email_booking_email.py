# Generated by Django 5.1.7 on 2025-03-22 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0009_testimonials_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testimonials',
            name='email',
        ),
        migrations.AddField(
            model_name='booking',
            name='email',
            field=models.EmailField(default='test@test.com', max_length=200),
        ),
    ]
