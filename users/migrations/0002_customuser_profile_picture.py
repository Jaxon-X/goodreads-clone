# Generated by Django 5.1.4 on 2024-12-18 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='profile_picture',
            field=models.ImageField(default='default.jpg', upload_to=''),
        ),
    ]
