# Generated by Django 2.0.7 on 2018-09-17 17:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20180917_1457'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='almoxarifado_relacionamento',
        ),
        migrations.RemoveField(
            model_name='user',
            name='departamento_relacionamento',
        ),
    ]
