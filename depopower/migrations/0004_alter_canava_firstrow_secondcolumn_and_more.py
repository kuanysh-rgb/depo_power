# Generated by Django 4.1.3 on 2022-11-16 10:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('depopower', '0003_canava'),
    ]

    operations = [
        migrations.AlterField(
            model_name='canava',
            name='firstRow_secondColumn',
            field=models.ForeignKey(default='Свободно', editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='firstRow_secondColumn', to='depopower.locomotive'),
        ),
        migrations.AlterField(
            model_name='canava',
            name='secondRow_firstColumn',
            field=models.ForeignKey(default='Профильное', on_delete=django.db.models.deletion.CASCADE, related_name='secondRow_firstColumn', to='depopower.locomotive'),
        ),
    ]
