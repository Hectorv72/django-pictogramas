# Generated by Django 2.2.4 on 2019-09-28 10:38

import PictoApp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PictoApp', '0006_auto_20190927_2116'),
    ]

    operations = [
        migrations.AddField(
            model_name='bdpictogramas',
            name='locucion',
            field=models.FileField(blank=True, null=True, upload_to=PictoApp.models.subir_sonido),
        ),
    ]
