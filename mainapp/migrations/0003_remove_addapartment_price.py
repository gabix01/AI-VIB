# Generated by Django 3.2.8 on 2021-11-23 06:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_auto_20211123_1137'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addapartment',
            name='price',
        ),
    ]
