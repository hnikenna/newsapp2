# Generated by Django 4.0.5 on 2022-07-12 19:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0020_remove_awarditem_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='awarditem',
            name='anon_id',
        ),
    ]