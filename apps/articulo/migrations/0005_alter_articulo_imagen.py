# Generated by Django 4.2.2 on 2023-07-05 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articulo', '0004_alter_articulo_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo',
            name='imagen',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='media/articulo'),
        ),
    ]
