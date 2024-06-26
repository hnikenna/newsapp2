# Generated by Django 4.1.1 on 2022-09-17 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0027_article_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.CharField(blank=True, choices=[('News', 'n')], max_length=50),
        ),
        migrations.AlterField(
            model_name='article',
            name='video',
            field=models.URLField(blank=True, null=True),
        ),
    ]
