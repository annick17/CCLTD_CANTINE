# Generated by Django 3.0.6 on 2020-06-12 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'permissions': (('supprimer_post', 'description supprimer un post'), ('dashboard_admin', 'accès django administrateur'), ('modifier_post', 'modifier un post'))},
        ),
        migrations.AlterField(
            model_name='post',
            name='accroche',
            field=models.CharField(max_length=200),
        ),
    ]
