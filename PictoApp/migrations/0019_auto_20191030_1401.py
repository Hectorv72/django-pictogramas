# Generated by Django 2.2.4 on 2019-10-30 17:01

import PictoApp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PictoApp', '0018_seguimiento_catelegida'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bdpictogramas',
            name='imagen',
            field=models.ImageField(blank=True, default='/PictoApp/media/imagenes/caballo.png', upload_to=PictoApp.models.subir_imagen),
        ),
        migrations.AlterField(
            model_name='bdpictogramas',
            name='locucion',
            field=models.FileField(blank=True, upload_to=PictoApp.models.subir_locucion),
        ),
    ]
