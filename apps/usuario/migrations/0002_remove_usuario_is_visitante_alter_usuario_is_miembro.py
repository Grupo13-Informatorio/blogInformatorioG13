# Generated by Django 4.2.2 on 2023-07-15 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='is_visitante',
        ),
        migrations.AlterField(
            model_name='usuario',
            name='is_miembro',
            field=models.BooleanField(default=True),
        ),
    ]