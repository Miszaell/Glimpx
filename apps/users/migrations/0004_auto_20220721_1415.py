# Generated by Django 3.2.5 on 2022-07-21 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20220721_1409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicaluser',
            name='date_of_birth',
            field=models.DateField(blank=True, default='1980-01-01', max_length=255, null=True, verbose_name='Fecha de nacimiento'),
        ),
        migrations.AlterField(
            model_name='user',
            name='date_of_birth',
            field=models.DateField(blank=True, default='1980-01-01', max_length=255, null=True, verbose_name='Fecha de nacimiento'),
        ),
    ]
