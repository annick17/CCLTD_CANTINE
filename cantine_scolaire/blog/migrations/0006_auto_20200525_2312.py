# Generated by Django 3.0.5 on 2020-05-25 21:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_post_accroche'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='date_de_création',
            new_name='date_de_creation',
        ),
    ]
