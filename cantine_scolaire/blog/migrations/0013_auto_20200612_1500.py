# Generated by Django 3.0.6 on 2020-06-12 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20200612_1444'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'permissions': (('ajouter_comment', 'ajouter un commentaire'), ('supprimer_comment', 'supprimer un commentaire'))},
        ),
    ]
