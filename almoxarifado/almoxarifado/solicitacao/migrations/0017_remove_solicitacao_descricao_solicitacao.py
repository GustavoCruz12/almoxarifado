# Generated by Django 2.0.7 on 2018-08-07 18:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('solicitacao', '0016_auto_20180807_1428'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='solicitacao',
            name='descricao_solicitacao',
        ),
    ]
