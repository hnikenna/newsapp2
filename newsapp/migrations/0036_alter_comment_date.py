# Generated by Django 4.1.1 on 2022-09-18 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0035_alter_article_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
