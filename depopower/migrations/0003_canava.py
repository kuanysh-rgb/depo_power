# Generated by Django 4.1.3 on 2022-11-16 09:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('depopower', '0002_delete_canava'),
    ]

    operations = [
        migrations.CreateModel(
            name='Canava',
            fields=[
                ('depo_name', models.TextField(default='rls-depo', max_length=144, primary_key=True, serialize=False, verbose_name='Name of DEPO')),
                ('firstRow_firstColumn', models.ForeignKey(default='Профильное', editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='firstRow_firstColumn', to='depopower.locomotive')),
                ('firstRow_secondColumn', models.ForeignKey(default='Свободно', on_delete=django.db.models.deletion.CASCADE, related_name='firstRow_secondColumn', to='depopower.locomotive')),
                ('firstRow_thirdColumn', models.ForeignKey(default='Свободно', on_delete=django.db.models.deletion.CASCADE, related_name='firstRow_thirdColumn', to='depopower.locomotive')),
                ('secondRow_firstColumn', models.ForeignKey(default='Профильное', editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='secondRow_firstColumn', to='depopower.locomotive')),
                ('secondRow_secondColumn', models.ForeignKey(default='Свободно', on_delete=django.db.models.deletion.CASCADE, related_name='secondRow_secondColumn', to='depopower.locomotive')),
                ('secondRow_thirdColumn', models.ForeignKey(default='Свободно', on_delete=django.db.models.deletion.CASCADE, related_name='secondRow_thirdColumn', to='depopower.locomotive')),
                ('thirdRow_firstColumn', models.ForeignKey(default='Свободно', on_delete=django.db.models.deletion.CASCADE, related_name='thirdRow_firstColumn', to='depopower.locomotive')),
                ('thirdRow_secondColumn', models.ForeignKey(default='Свободно', on_delete=django.db.models.deletion.CASCADE, related_name='thirdRow_secondColumn', to='depopower.locomotive')),
                ('thirdRow_thirdColumn', models.ForeignKey(default='Свободно', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='thirdRow_thirdColumn', to='depopower.locomotive')),
            ],
            options={
                'verbose_name': 'Canava',
                'verbose_name_plural': 'Canavas',
            },
        ),
    ]
