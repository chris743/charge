# Generated by Django 4.0.5 on 2022-06-11 17:23

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BagCost',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('description', models.TextField(null=True)),
                ('bagWeight', models.FloatField(default=0)),
                ('costPerBag', models.FloatField(default=0)),
                ('bagLength', models.FloatField(default=0)),
                ('wastePercentage', models.FloatField(default=0)),
                ('laborCost', models.FloatField(default=0)),
                ('totalCost', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='BagType',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('bagType', models.CharField(max_length=50, null=True)),
                ('description', models.TextField(null=True)),
                ('miscCharges', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='BoxDifference',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=25)),
                ('boxDiff', models.FloatField(default=0)),
                ('description', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Commodities',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('description', models.CharField(max_length=30)),
                ('avgCtnPrice', models.FloatField(default=0)),
                ('stdCtnCost', models.FloatField(default=0)),
                ('netWeightChile', models.FloatField(default=0)),
                ('netWeightDomestic', models.FloatField(default=0)),
                ('packingCharge', models.FloatField(default=0)),
                ('pallets', models.FloatField(default=0)),
                ('profitPerBag', models.FloatField(default=0)),
                ('promo', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Packaging',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('description', models.CharField(max_length=50)),
                ('cost', models.FloatField(default=0)),
            ],
        ),
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
                ('bagType', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='charge.bagtype')),
                ('commodity', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='charge.commodities')),
                ('referring_bagCost', models.ForeignKey(db_constraint=False, default=1, on_delete=django.db.models.deletion.CASCADE, to='charge.bagcost')),
            ],
        ),
        migrations.CreateModel(
            name='PackagingCosts',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('filmCostPerMeter', models.FloatField(default=0)),
                ('netCostPerMeter', models.FloatField(default=0)),
                ('vexarClipCost', models.FloatField(default=0)),
                ('miscCost', models.FloatField(default=0)),
                ('bagType', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='charge.bagtype')),
            ],
        ),
        migrations.AddField(
            model_name='bagcost',
            name='bagType',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='charge.bagtype'),
        ),
    ]
