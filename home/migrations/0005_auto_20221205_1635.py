# Generated by Django 3.2 on 2022-12-05 16:35

from django.db import migrations
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20221205_1552'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='cover',
            field=stdimage.models.StdImageField(blank=True, force_min_size=False, null=True, upload_to='cover', variations={'thumb': {'crop': True, 'height': 520, 'width': 770}}, verbose_name='Imagem'),
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=stdimage.models.StdImageField(blank=True, force_min_size=False, null=True, upload_to='property', variations={'thumb': {'crop': True, 'height': 520, 'width': 770}}, verbose_name='Imagem'),
        ),
    ]