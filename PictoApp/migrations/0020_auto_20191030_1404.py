# Generated by Django 2.2.4 on 2019-10-30 17:04

import PictoApp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PictoApp', '0019_auto_20191030_1401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bdpictogramas',
            name='imagen',
            field=models.ImageField(upload_to=PictoApp.models.subir_imagen),
        ),
        migrations.AlterField(
            model_name='bdpictogramas',
            name='locucion',
            field=models.FileField(upload_to=PictoApp.models.subir_locucion),
        ),
    ]
