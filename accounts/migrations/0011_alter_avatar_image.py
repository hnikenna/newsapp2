# Generated by Django 4.0.5 on 2022-06-29 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_alter_profile_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avatar',
            name='image',
            field=models.ImageField(blank=True, default='../static/img/user.png', null=True, upload_to='articles'),
        ),
    ]
