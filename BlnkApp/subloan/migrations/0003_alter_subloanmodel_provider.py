# Generated by Django 4.2.8 on 2023-12-21 12:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('loan_provider', '0001_initial'),
        ('subloan', '0002_subloanmodel_amount_to_pay_subloanmodel_current_paid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subloanmodel',
            name='provider',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='provider_id', to='loan_provider.loanprovidermodel'),
        ),
    ]
