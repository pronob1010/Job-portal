# Generated by Django 3.1.5 on 2021-01-31 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_auto_20210131_2021'),
    ]

    operations = [
        migrations.AddField(
            model_name='freelancer_job',
            name='freelancer_slug',
            field=models.SlugField(default=models.CharField(max_length=200), max_length=100),
        ),
    ]
