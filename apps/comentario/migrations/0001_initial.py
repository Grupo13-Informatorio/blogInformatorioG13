# Generated by Django 4.2.2 on 2023-07-10 17:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('articulo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenido', models.CharField(default='', help_text='Ingrese aqui su comentario', max_length=100, verbose_name='Texto')),
                ('modificado', models.DateField(blank=True, editable=False, null=True, verbose_name='Modificado')),
                ('creado', models.DateField(editable=False, verbose_name='Fecha de publicacion')),
                ('imagen', models.ImageField(default=None, upload_to='media/images/')),
                ('articulo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='articulo.articulo', verbose_name='Articulo')),
                ('id_comentario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comentario_comentado', to='comentario.comentario')),
            ],
        ),
    ]
