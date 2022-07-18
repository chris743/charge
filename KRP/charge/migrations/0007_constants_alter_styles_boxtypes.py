# Generated by Django 4.0.1 on 2022-07-18 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charge', '0006_alter_boxdifference_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Constants',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True)),
                ('value', models.FloatField(default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='styles',
            name='boxTypes',
            field=models.ManyToManyField(to='charge.BoxDifference'),
        ),
    ]
