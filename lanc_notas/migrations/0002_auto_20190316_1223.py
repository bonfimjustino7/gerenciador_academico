# Generated by Django 2.1.7 on 2019-03-16 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lanc_notas', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aluno_diciplina',
            name='Turma_Diciplina',
        ),
        migrations.AddField(
            model_name='aluno_diciplina',
            name='situacao',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
