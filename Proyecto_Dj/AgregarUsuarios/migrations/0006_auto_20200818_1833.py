# Generated by Django 3.1 on 2020-08-18 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AgregarUsuarios', '0005_auto_20200812_1125'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='roll',
        ),
        migrations.AlterField(
            model_name='usuario',
            name='password',
            field=models.CharField(max_length=30),
        ),
    ]
