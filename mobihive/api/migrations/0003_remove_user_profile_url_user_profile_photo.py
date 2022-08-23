# Generated by Django 4.1 on 2022-08-23 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_user_profile_photo_user_profile_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='profile_url',
        ),
        migrations.AddField(
            model_name='user',
            name='profile_photo',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pic'),
        ),
    ]