# Generated by Django 4.2.2 on 2023-06-29 19:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articulo', '0007_categoria_remove_articulo_genero_delete_genero_and_more'),
        ('comentario', '0005_alter_comentario_articulo_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comentario',
            name='comentario',
        ),
        migrations.AddField(
            model_name='comentario',
            name='contenido',
            field=models.CharField(default='', help_text='Ingrese aqui su comentario', max_length=100, verbose_name='Texto'),
        ),
        migrations.AddField(
            model_name='comentario',
            name='imagen',
            field=models.ImageField(default=None, upload_to='media/images/'),
        ),
        migrations.AlterField(
            model_name='comentario',
            name='articulo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='articulo.articulo', verbose_name='Articulo'),
        ),
    ]
