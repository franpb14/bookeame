# Generated by Django 3.1.2 on 2021-01-14 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0018_todostuslibros_categorias'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlanetaLibros',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.TextField()),
                ('isbn', models.IntegerField()),
                ('recomendado', models.BooleanField()),
                ('precio', models.TextField()),
                ('autor', models.TextField()),
                ('categorias', models.TextField()),
                ('urlImagen', models.URLField()),
                ('fechapublicacion', models.DateTimeField()),
                ('descripcionHTML', models.TextField()),
                ('urlCompra', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='tematicas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('principal', models.TextField(help_text='Introduce el nombre de la temática principal')),
                ('secundaria', models.TextField(help_text='Introduce el nombre de la temática secundaria')),
            ],
        ),
    ]
