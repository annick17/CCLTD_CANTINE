# Generated by Django 3.0.5 on 2020-05-23 18:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200523_1943'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='accroche',
        ),
    ]
