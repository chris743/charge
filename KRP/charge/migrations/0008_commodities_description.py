# Generated by Django 4.0.4 on 2022-05-30 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charge', '0007_commodities'),
    ]

    operations = [
        migrations.AddField(
            model_name='commodities',
            name='description',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]