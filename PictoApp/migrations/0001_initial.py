# Generated by Django 2.2.4 on 2019-09-25 16:08

import PictoApp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Imagen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=30)),
                ('imagen', models.FileField(upload_to=PictoApp.models.subir_imagen)),
            ],
        ),
    ]