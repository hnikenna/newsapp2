# Generated by Django 4.0.5 on 2022-07-01 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_alter_profile_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, default='static_media/user.png', null=True, upload_to='articles'),
        ),
    ]
