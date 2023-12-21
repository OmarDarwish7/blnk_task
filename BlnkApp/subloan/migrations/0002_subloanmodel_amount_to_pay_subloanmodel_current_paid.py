# Generated by Django 4.2.8 on 2023-12-21 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subloan', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subloanmodel',
            name='amount_to_pay',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='subloanmodel',
            name='current_paid',
            field=models.FloatField(default=0.0),
        ),
    ]
