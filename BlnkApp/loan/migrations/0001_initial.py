# Generated by Django 4.2.8 on 2023-12-20 14:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='LoanModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('interest_rate', models.FloatField()),
                ('bank_percentage', models.FloatField()),
                ('term', models.IntegerField()),
                ('status', models.CharField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='loan_customer', to=settings.AUTH_USER_MODEL)),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='loan_provider', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
