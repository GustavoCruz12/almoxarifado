# Generated by Django 2.0.7 on 2018-09-17 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secretaria', '0001_initial'),
        ('users', '0007_auto_20180914_0956'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='almoxarifado_relacionamento',
            field=models.ForeignKey(blank=True, default=0, on_delete=None, to='secretaria.Almoxarifado'),
        ),
        migrations.AddField(
            model_name='user',
            name='departamento_relacionamento',
            field=models.ForeignKey(blank=True, default=0, on_delete=None, to='secretaria.Departamento'),
        ),
    ]
