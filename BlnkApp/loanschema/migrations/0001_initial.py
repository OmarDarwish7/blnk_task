# Generated by Django 4.2.8 on 2023-12-21 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LoanSchemaModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('min_amount', models.FloatField()),
                ('max_amount', models.FloatField()),
                ('interest_rate', models.FloatField()),
                ('term', models.IntegerField()),
            ],
        ),
    ]