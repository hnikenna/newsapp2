# Generated by Django 4.0.5 on 2022-07-12 19:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('newsapp', '0018_remove_awarditem_type_awarditem_anon_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='awarditem',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
