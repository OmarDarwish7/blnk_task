# Generated by Django 4.2.8 on 2023-12-21 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loan', '0004_rename_total_amount_loanmodel_amount_after_interest_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='loanmodel',
            name='monthly_amount',
            field=models.FloatField(default=0.0),
            preserve_default=False,
        ),
    ]