# Generated by Django 4.2.2 on 2023-06-29 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articulo', '0007_categoria_remove_articulo_genero_delete_genero_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='articulo',
            name='imagen',
            field=models.ImageField(default=None, upload_to='media/images/'),
        ),
    ]
