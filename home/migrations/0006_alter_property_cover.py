# Generated by Django 3.2 on 2022-12-05 18:53

from django.db import migrations
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20221205_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='cover',
            field=stdimage.models.StdImageField(blank=True, force_min_size=False, null=True, upload_to='cover', variations={'thumb': {'crop': True, 'height': 250, 'width': 370}}, verbose_name='Imagem'),
        ),
    ]