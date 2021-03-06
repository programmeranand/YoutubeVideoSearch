# Generated by Django 3.0.8 on 2020-07-05 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('key', models.CharField(max_length=128, unique=True)),
                ('value', models.CharField(blank=True, default='', max_length=512)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='YoutubeVideo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('channel_id', models.CharField(db_index=True, max_length=50, unique=True)),
                ('channel_title', models.CharField(blank=True, max_length=400, null=True)),
                ('video_id', models.CharField(db_index=True, max_length=30, unique=True)),
                ('video_title', models.CharField(blank=True, max_length=300, null=True)),
                ('video_description', models.TextField(blank=True, null=True)),
                ('video_thumbnail', models.URLField(blank=True, null=True)),
                ('video_publish_date', models.DateTimeField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
