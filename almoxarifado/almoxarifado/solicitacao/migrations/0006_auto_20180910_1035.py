# Generated by Django 2.0.7 on 2018-09-10 13:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('solicitacao', '0005_auto_20180910_1034'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='solicitacao',
            options={'permissions': (('administrativo_permissao', 'pode acessar adm'), ('entrega_permissao', 'pode acessar entrega')), 'verbose_name': 'Solicitação', 'verbose_name_plural': 'Solicitações'},
        ),
    ]