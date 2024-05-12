# Generated by Django 4.0.4 on 2022-05-28 22:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Award',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='AwardItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('award_quantity', models.PositiveIntegerField(default=0)),
                ('award', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='newsapp.award')),
            ],
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('yes_vote', models.IntegerField(default=0)),
                ('no_vote', models.IntegerField(default=0)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('award', models.ManyToManyField(blank=True, to='newsapp.awarditem')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('yes_vote', models.IntegerField(default=0)),
                ('no_vote', models.IntegerField(default=0)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('award', models.ManyToManyField(blank=True, to='newsapp.awarditem')),
                ('reply', models.ManyToManyField(blank=True, to='newsapp.reply')),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('header_text', models.CharField(blank=True, max_length=250)),
                ('content', models.TextField()),
                ('slug', models.SlugField(blank=True, max_length=100, unique=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('is_draft', models.BooleanField(default=True)),
                ('image', models.ImageField(blank=True, upload_to='articles')),
                ('source_url', models.URLField(blank=True)),
                ('source_name', models.CharField(max_length=200)),
                ('yes_vote', models.IntegerField(default=0)),
                ('no_vote', models.IntegerField(default=0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('comment', models.ManyToManyField(blank=True, null=True, to='newsapp.comment')),
            ],
        ),
    ]
