# Generated by Django 4.0.5 on 2022-06-17 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charge', '0011_alter_styles_referring_miscpackaging'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='styles',
            name='referring_miscPackaging',
        ),
        migrations.AddField(
            model_name='styles',
            name='referring_miscPackaging',
            field=models.ManyToManyField(db_constraint=False, null=True, to='charge.miscpackaging'),
        ),
    ]
