# Generated by Django 4.1.3 on 2022-11-27 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('depopower', '0008_cellrecord'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cellrecord',
            name='volume',
            field=models.DecimalField(decimal_places=1, max_digits=3, verbose_name='Volume'),
        ),
    ]