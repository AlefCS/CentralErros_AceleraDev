# Generated by Django 3.0.8 on 2020-07-18 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('errors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='error',
            name='layer',
            field=models.CharField(choices=[('B', 'BACKEND'), ('F', 'FRONTEND'), ('A', 'APPLICATION'), ('D', 'DESKTOP')], max_length=25, verbose_name='Camada'),
        ),
    ]
