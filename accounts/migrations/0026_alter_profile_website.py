# Generated by Django 4.0.5 on 2022-07-09 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0025_alter_profile_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='website',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
    ]
