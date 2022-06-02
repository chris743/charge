# Generated by Django 4.0.4 on 2022-05-29 04:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('charge', '0002_bagcost_rename_bagtype_boxtype'),
    ]

    operations = [
        migrations.AddField(
            model_name='bagcost',
            name='bagLength',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='bagcost',
            name='bagWeight',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='bagcost',
            name='boxType',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='charge.boxtype'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bagcost',
            name='costPerBag',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='bagcost',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='bagcost',
            name='laborCost',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='bagcost',
            name='totalCost',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='bagcost',
            name='wastePercentage',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='boxtype',
            name='boxType',
            field=models.CharField(max_length=50, null=True),
        ),
    ]