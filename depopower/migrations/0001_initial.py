# Generated by Django 4.1.3 on 2022-11-16 09:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AvailableTechwork',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('to_name', models.TextField(default='None', max_length=144, verbose_name='Name of TO')),
            ],
            options={
                'verbose_name': 'AvailableTechwork',
                'verbose_name_plural': 'AvailableTechworks',
            },
        ),
        migrations.CreateModel(
            name='Locomotive',
            fields=[
                ('model_name', models.TextField(primary_key=True, serialize=False, verbose_name='Name of Model')),
                ('sections', models.DecimalField(decimal_places=0, max_digits=3, verbose_name='Count of sectioins')),
            ],
            options={
                'verbose_name': 'Locomotive',
                'verbose_name_plural': 'Locomotives',
            },
        ),
        migrations.CreateModel(
            name='MonthWorkDay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(default='2023', verbose_name='Year')),
                ('month', models.TextField(default='Jan', verbose_name='Month')),
                ('workdays', models.DecimalField(decimal_places=0, max_digits=3, verbose_name='Count of workdays')),
            ],
            options={
                'verbose_name': 'MonthWorkDay',
                'verbose_name_plural': 'MonthWorkDays',
                'unique_together': {('year', 'month')},
            },
        ),
        migrations.CreateModel(
            name='Canava',
            fields=[
                ('depo_name', models.TextField(default='rls-depo', max_length=144, primary_key=True, serialize=False, verbose_name='Name of DEPO')),
                ('firstRow_firstColumn', models.ForeignKey(default='????????????????????', editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='firstRow_firstColumn', to='depopower.locomotive')),
                ('firstRow_secondColumn', models.ForeignKey(default='????????????????', on_delete=django.db.models.deletion.CASCADE, related_name='firstRow_secondColumn', to='depopower.locomotive')),
                ('firstRow_thirdColumn', models.ForeignKey(default='????????????????', on_delete=django.db.models.deletion.CASCADE, related_name='firstRow_thirdColumn', to='depopower.locomotive')),
                ('secondRow_firstColumn', models.ForeignKey(default='????????????????????', editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='secondRow_firstColumn', to='depopower.locomotive')),
                ('secondRow_secondColumn', models.ForeignKey(default='????????????????', on_delete=django.db.models.deletion.CASCADE, related_name='secondRow_secondColumn', to='depopower.locomotive')),
                ('secondRow_thirdColumn', models.ForeignKey(default='????????????????', on_delete=django.db.models.deletion.CASCADE, related_name='secondRow_thirdColumn', to='depopower.locomotive')),
                ('thirdRow_firstColumn', models.ForeignKey(default='????????????????', on_delete=django.db.models.deletion.CASCADE, related_name='thirdRow_firstColumn', to='depopower.locomotive')),
                ('thirdRow_secondColumn', models.ForeignKey(default='????????????????', on_delete=django.db.models.deletion.CASCADE, related_name='thirdRow_secondColumn', to='depopower.locomotive')),
                ('thirdRow_thirdColumn', models.ForeignKey(default='????????????????', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='thirdRow_thirdColumn', to='depopower.locomotive')),
            ],
            options={
                'verbose_name': 'Canava',
                'verbose_name_plural': 'Canavas',
            },
        ),
        migrations.CreateModel(
            name='TechWork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('to_name', models.TextField(default='None', max_length=144, verbose_name='Name of TO')),
                ('hours', models.DecimalField(decimal_places=1, max_digits=4, verbose_name='Count of hours')),
                ('days', models.FloatField(default=0, editable=False, verbose_name='Count of days')),
                ('model_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='depopower.locomotive')),
            ],
            options={
                'verbose_name': 'TechWork',
                'verbose_name_plural': 'TechWorks',
                'unique_together': {('to_name', 'model_name')},
            },
        ),
    ]
