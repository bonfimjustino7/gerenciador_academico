# Generated by Django 2.1.7 on 2019-06-30 01:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lanc_notas', '0019_auto_20190629_2224'),
    ]

    operations = [
        migrations.RenameField(
            model_name='diciplina',
            old_name='diciplina',
            new_name='nome_diciplina',
        ),
    ]
