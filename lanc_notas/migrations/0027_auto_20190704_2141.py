# Generated by Django 2.1.7 on 2019-07-05 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lanc_notas', '0026_auto_20190702_2128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno_diciplina',
            name='n1',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=4),
        ),
        migrations.AlterField(
            model_name='aluno_diciplina',
            name='n2',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=4),
        ),
        migrations.AlterField(
            model_name='aluno_diciplina',
            name='n3',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=4),
        ),
    ]
