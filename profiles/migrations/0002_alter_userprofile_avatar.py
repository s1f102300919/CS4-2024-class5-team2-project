# Generated by Django 5.1.4 on 2025-01-10 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(blank=True, default='avatars/default.png', null=True, upload_to='avatars/'),
        ),
    ]
