# Generated by Django 3.2.8 on 2021-11-21 13:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='addapartment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('appname', models.CharField(max_length=800)),
                ('area', models.CharField(max_length=800)),
                ('owner', models.CharField(max_length=800)),
                ('price', models.CharField(max_length=800)),
                ('image', models.FileField(null=True, upload_to='image/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
