# Generated by Django 3.1.5 on 2021-01-31 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='Organization',
            field=models.BooleanField(default=False),
        ),
    ]