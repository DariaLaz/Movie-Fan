# Generated by Django 5.0 on 2023-12-26 16:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('year', models.IntegerField()),
                ('genre', models.CharField(max_length=50)),
                ('tumbnail', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('score', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=6, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('host', models.CharField(max_length=50, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('categories', models.ManyToManyField(related_name='games', to='api.category')),
                ('players', models.ManyToManyField(related_name='games', to='api.player')),
            ],
        ),
        migrations.CreateModel(
            name='Submition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.movie')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.player')),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='submitions',
            field=models.ManyToManyField(related_name='categories', to='api.submition'),
        ),
    ]