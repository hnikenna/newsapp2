# Generated by Django 4.1.1 on 2022-10-30 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0036_alter_comment_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reply',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]