# Generated by Django 4.0.4 on 2022-05-29 04:58

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('charge', '0005_alter_bagcost_baglength_alter_bagcost_bagweight_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PackagingCosts',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('filmCostPerMeter', models.FloatField(default=0)),
                ('netCostPerMeter', models.FloatField(default=0)),
                ('vexarClipCost', models.FloatField(default=0)),
                ('miscCost', models.FloatField(default=0)),
                ('boxType', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='charge.boxtype')),
            ],
        ),
    ]