# Generated by Django 3.0.5 on 2020-04-06 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0007_auto_20200407_0458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visit',
            name='category',
            field=models.CharField(choices=[('Residential', 'Residential'), ('Workplace', 'Workplace'), ('Visit', 'Visit')], max_length=20),
        ),
    ]
