# Generated by Django 3.0.7 on 2020-06-28 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_auto_20200627_0833'),
    ]

    operations = [
        migrations.AddField(
            model_name='color',
            name='button_url',
            field=models.URLField(default='', max_length=2000),
        ),
    ]
