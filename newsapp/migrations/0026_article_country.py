# Generated by Django 4.0.6 on 2022-09-10 01:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0025_rename_flag_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='country',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='newsapp.country'),
        ),
    ]
