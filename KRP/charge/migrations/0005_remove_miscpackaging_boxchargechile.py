# Generated by Django 4.0.5 on 2022-07-15 16:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('charge', '0004_alter_styles_bagsize_alter_styles_twb_flag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='miscpackaging',
            name='boxChargeChile',
        ),
    ]
