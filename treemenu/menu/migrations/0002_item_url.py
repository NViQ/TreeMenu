# Generated by Django 4.1.7 on 2023-03-01 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='url',
            field=models.CharField(default='/menu', max_length=255, verbose_name='Urls'),
        ),
    ]
