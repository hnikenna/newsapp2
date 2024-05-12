# Generated by Django 4.0.5 on 2022-07-12 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0016_article_anon_id_reply_anon_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='award',
        ),
        migrations.RemoveField(
            model_name='reply',
            name='award',
        ),
        migrations.AddField(
            model_name='awarditem',
            name='parent_id',
            field=models.CharField(blank=True, default='', max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='awarditem',
            name='type',
            field=models.CharField(blank=True, default='', max_length=1, null=True),
        ),
    ]
