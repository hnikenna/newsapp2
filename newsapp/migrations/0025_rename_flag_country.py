# Generated by Django 4.0.6 on 2022-09-09 22:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0024_flag_alter_award_animation_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Flag',
            new_name='Country',
        ),
    ]
