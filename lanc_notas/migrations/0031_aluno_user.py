# Generated by Django 2.1.7 on 2019-07-06 14:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lanc_notas', '0030_auto_20190704_2300'),
    ]

    operations = [
        migrations.AddField(
            model_name='aluno',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
