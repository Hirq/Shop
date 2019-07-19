# Generated by Django 2.0.7 on 2019-07-19 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Effect',
            fields=[
                ('effect_id', models.AutoField(primary_key=True, serialize=False)),
                ('effect_name', models.CharField(max_length=80)),
                ('effect_price', models.IntegerField(default=50)),
                ('effect_description', models.CharField(max_length=400)),
                ('effect_count', models.IntegerField(default=1)),
                ('effect_group', models.CharField(choices=[('DIS', 'DISTORTION'), ('OCT', 'OCTAVER'), ('COM', 'COMPRESOR')], max_length=3)),
                ('effect_photo', models.ImageField(blank=True, null=True, upload_to='images')),
                ('slug', models.SlugField(default=1, max_length=200)),
            ],
        ),
    ]
