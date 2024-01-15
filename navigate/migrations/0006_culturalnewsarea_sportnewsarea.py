# Generated by Django 4.1.3 on 2023-02-04 21:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('navigate', '0005_culturalnews_sportnews'),
    ]

    operations = [
        migrations.CreateModel(
            name='CulturalNewsArea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='pics')),
                ('tag', models.CharField(max_length=100)),
                ('url', models.URLField(null=True)),
                ('heading', models.CharField(max_length=100)),
                ('date', models.DateField(verbose_name=datetime.date)),
            ],
        ),
        migrations.CreateModel(
            name='SportNewsArea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='pics')),
                ('tag', models.CharField(max_length=100)),
                ('url', models.URLField(null=True)),
                ('heading', models.CharField(max_length=100)),
                ('date', models.DateField(verbose_name=datetime.date)),
            ],
        ),
    ]