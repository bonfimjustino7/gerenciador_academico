# Generated by Django 2.1.7 on 2019-06-22 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lanc_notas', '0013_auto_20190622_1109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno_diciplina',
            name='n1',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4),
        ),
        migrations.AlterField(
            model_name='aluno_diciplina',
            name='n2',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4),
        ),
        migrations.AlterField(
            model_name='aluno_diciplina',
            name='n3',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4),
        ),
    ]