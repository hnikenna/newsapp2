# Generated by Django 4.1.1 on 2022-09-17 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0028_article_category_alter_article_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.CharField(blank=True, choices=[('n', 'News')], max_length=50),
        ),
    ]
