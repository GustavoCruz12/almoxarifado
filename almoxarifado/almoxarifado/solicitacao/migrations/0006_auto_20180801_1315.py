# Generated by Django 2.0.7 on 2018-08-01 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solicitacao', '0005_auto_20180801_1311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitacao',
            name='descricao_solicitacao',
            field=models.CharField(max_length=255, verbose_name='Descrição da Solicitacao'),
        ),
    ]
