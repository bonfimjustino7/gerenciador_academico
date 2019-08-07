# Generated by Django 2.1.7 on 2019-06-22 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lanc_notas', '0009_auto_20190622_1058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno_diciplina',
            name='faltas',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='aluno_diciplina',
            name='n1',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True),
        ),
        migrations.AlterField(
            model_name='aluno_diciplina',
            name='n2',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True),
        ),
        migrations.AlterField(
            model_name='aluno_diciplina',
            name='n3',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True),
        ),
    ]