# Generated by Django 3.1 on 2020-08-12 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AgregarUsuarios', '0004_auto_20200812_1110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
    ]
