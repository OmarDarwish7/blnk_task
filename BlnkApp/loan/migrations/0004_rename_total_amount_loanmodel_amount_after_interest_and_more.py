# Generated by Django 4.2.8 on 2023-12-21 11:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loan', '0003_loanmodel_amount_paid_loanmodel_amount_to_pay_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='loanmodel',
            old_name='total_amount',
            new_name='amount_after_interest',
        ),
        migrations.RenameField(
            model_name='loanmodel',
            old_name='amount',
            new_name='requested_amount',
        ),
    ]