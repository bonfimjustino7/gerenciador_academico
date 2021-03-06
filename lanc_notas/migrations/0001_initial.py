# Generated by Django 2.1.7 on 2019-03-16 15:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('matricula', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=50)),
                ('data_nac', models.CharField(max_length=12, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Aluno_Diciplina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('n1', models.DecimalField(decimal_places=2, max_digits=4)),
                ('n2', models.DecimalField(decimal_places=2, max_digits=4)),
                ('n3', models.DecimalField(decimal_places=2, max_digits=4)),
                ('media', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Diciplina',
            fields=[
                ('cod_diciplina', models.AutoField(primary_key=True, serialize=False)),
                ('nome_diciplina', models.CharField(max_length=30)),
                ('nota_aprovacao', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
        ),
        migrations.CreateModel(
            name='Turma',
            fields=[
                ('cod_turma', models.AutoField(primary_key=True, serialize=False)),
                ('semestre', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Turma_Diciplina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod_diciplina', models.ManyToManyField(to='lanc_notas.Diciplina')),
                ('cod_turma', models.ManyToManyField(to='lanc_notas.Turma')),
            ],
        ),
        migrations.AddField(
            model_name='aluno_diciplina',
            name='Turma_Diciplina',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lanc_notas.Turma_Diciplina'),
        ),
        migrations.AddField(
            model_name='aluno_diciplina',
            name='aluno',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lanc_notas.Aluno'),
        ),
        migrations.AddField(
            model_name='aluno_diciplina',
            name='diciplina',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lanc_notas.Diciplina'),
        ),
        migrations.AddField(
            model_name='aluno',
            name='semestre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lanc_notas.Turma'),
        ),
    ]
