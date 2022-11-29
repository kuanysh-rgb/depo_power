# Generated by Django 4.1.3 on 2022-11-29 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('depopower', '0013_alter_cellrecord_volume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cellrecord',
            name='volume',
            field=models.DecimalField(decimal_places=1, default=0, editable=False, max_digits=3, verbose_name='Volume'),
        ),
    ]