# Generated by Django 4.0.5 on 2022-06-18 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0005_voteitem_article_voteitem_comment_voteitem_reply'),
    ]

    operations = [
        migrations.AddField(
            model_name='award',
            name='price',
            field=models.IntegerField(default='500'),
        ),
    ]
