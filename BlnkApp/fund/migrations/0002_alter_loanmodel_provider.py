# Generated by Django 4.2.8 on 2023-12-20 15:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('loan_provider', '0001_initial'),
        ('fund', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loanmodel',
            name='provider',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='loan_provider', to='loan_provider.loanprovidermodel'),
        ),
    ]
