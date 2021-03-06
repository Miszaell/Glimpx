# Generated by Django 3.2.5 on 2022-07-04 21:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=250)),
                ('quantity', models.IntegerField()),
                ('uom', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distinctive_denmination', models.CharField(max_length=250)),
                ('generic_denomination', models.CharField(max_length=250)),
                ('pharmaceutical_denomination', models.CharField(max_length=250)),
                ('drug_concentration', models.CharField(max_length=250)),
                ('formula', models.CharField(max_length=250)),
                ('route_administration', models.CharField(max_length=250)),
                ('precautions', models.CharField(max_length=250)),
                ('quantity', models.IntegerField()),
                ('uom', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.material')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.medicine')),
            ],
        ),
    ]
