# Generated by Django 4.1.1 on 2022-09-17 13:29

from django.db import migrations
import django_bleach.models


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0032_alter_article_category_alter_reply_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=django_bleach.models.BleachField(),
        ),
    ]
