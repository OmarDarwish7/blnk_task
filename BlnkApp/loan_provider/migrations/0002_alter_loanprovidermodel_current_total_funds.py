# Generated by Django 4.2.8 on 2023-12-21 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loan_provider', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loanprovidermodel',
            name='current_total_funds',
            field=models.FloatField(),
        ),
    ]
