# Generated by Django 3.2.5 on 2022-07-03 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicaluser',
            name='email',
            field=models.EmailField(db_index=True, max_length=255, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='historicaluser',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Nombre(s)'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=255, unique=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Nombre(s)'),
        ),
    ]
