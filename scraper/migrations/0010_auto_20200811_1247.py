# Generated by Django 3.0 on 2020-08-11 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0009_notification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=400),
        ),
    ]
