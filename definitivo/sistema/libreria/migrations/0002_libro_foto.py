# Generated by Django 4.2.2 on 2023-07-08 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='libro',
            name='foto',
            field=models.ImageField(null=True, upload_to='imagenes/', verbose_name='Foto'),
        ),
    ]
