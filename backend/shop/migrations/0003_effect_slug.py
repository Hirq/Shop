# Generated by Django 2.0.7 on 2019-06-09 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20180722_2305'),
    ]

    operations = [
        migrations.AddField(
            model_name='effect',
            name='slug',
            field=models.SlugField(default=1, max_length=200),
        ),
    ]
