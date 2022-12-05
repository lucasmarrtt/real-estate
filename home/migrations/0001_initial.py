# Generated by Django 3.2 on 2022-08-15 19:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import stdimage.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagem', stdimage.models.StdImageField(force_min_size=False, upload_to='Agent', variations={'thumb': {'crop': True, 'height': 400, 'width': 380}}, verbose_name='Imagem')),
                ('name', models.CharField(max_length=255, verbose_name='Nome do corretor')),
                ('number', models.CharField(max_length=255, verbose_name='Telefone')),
                ('facebook', models.URLField(verbose_name='Facebook')),
                ('instagram', models.URLField(verbose_name='Instagram')),
                ('whatsapp', models.URLField(verbose_name='WhatsApp')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nome da categoria')),
                ('icon', models.CharField(choices=[('icon-1', 'residencial'), ('icon-2', 'comercial'), ('icon-3', 'industrial'), ('icon-4', 'rural')], max_length=255, verbose_name='Icone')),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Título')),
                ('slug', models.SlugField(blank=True, max_length=255, null=True, unique=True, verbose_name='Slug')),
                ('content', models.TextField()),
                ('price', models.IntegerField()),
                ('address', models.TextField()),
                ('rooms', models.IntegerField(verbose_name='Quartos')),
                ('bathrooms', models.IntegerField(verbose_name='Banheiros')),
                ('garage_size', models.IntegerField(verbose_name='Vagas na garagem')),
                ('area', models.IntegerField(verbose_name='Área')),
                ('city', models.CharField(max_length=255, verbose_name='Cidade')),
                ('state', models.CharField(max_length=255, verbose_name='Estado')),
                ('zipcode', models.CharField(max_length=255, verbose_name='CEP')),
                ('google_maps', models.TextField()),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.agent')),
                ('ctagory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.category')),
            ],
        ),
    ]
