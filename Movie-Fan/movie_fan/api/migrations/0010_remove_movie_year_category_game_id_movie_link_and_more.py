# Generated by Django 5.0 on 2024-01-21 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_category_mode'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='year',
        ),
        migrations.AddField(
            model_name='category',
            name='game_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='movie',
            name='link',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AddField(
            model_name='movie',
            name='rating',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='movie',
            name='tumbnail',
            field=models.CharField(max_length=300),
        ),
    ]