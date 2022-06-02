# Generated by Django 4.0.4 on 2022-06-01 17:14

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('charge', '0008_commodities_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Styles',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('twb_flag', models.BooleanField(null=True)),
                ('count', models.IntegerField(default=0)),
                ('bagSize', models.IntegerField(default=0)),
                ('weight', models.FloatField(default=0)),
                ('flag', models.IntegerField(default=0)),
                ('countSize', models.CharField(max_length=200)),
                ('domesticSalesCost', models.IntegerField(default=0)),
                ('chileanSalesCost', models.FloatField(default=0)),
                ('boxType', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='charge.boxtype')),
                ('commodity', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='charge.commodities')),
            ],
        ),
    ]