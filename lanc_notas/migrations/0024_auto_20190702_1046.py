# Generated by Django 2.1.7 on 2019-07-02 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lanc_notas', '0023_auto_20190702_1038'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='turma',
            name='aberto',
        ),
        migrations.AddField(
            model_name='aluno_diciplina',
            name='semestre_aberto',
            field=models.BooleanField(default=False),
        ),
    ]