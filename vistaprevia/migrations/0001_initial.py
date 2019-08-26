# Generated by Django 2.2.3 on 2019-08-24 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(db_index=True, max_length=100)),
                ('slug', models.SlugField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producto', models.CharField(max_length=200)),
                ('fecha_publicacion', models.DateTimeField(verbose_name='Fecha de publicación')),
                ('ruta_imagen', models.FileField(blank=True, default='defecto/defecto.jpg', null=True, upload_to='fotos/%Y/%m/%d')),
                ('estado', models.CharField(choices=[('Borrador', 'Borrador'), ('Publicado', 'Publicado'), ('Retirado', 'Retirado')], default='Borrador', max_length=10)),
                ('categoria', models.ManyToManyField(to='vistaprevia.Categoria')),
            ],
        ),
    ]
