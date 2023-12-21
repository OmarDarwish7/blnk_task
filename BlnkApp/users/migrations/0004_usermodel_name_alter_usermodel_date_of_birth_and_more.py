# Generated by Django 4.2.8 on 2023-12-20 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_usermodel_national_id_usermodel_user_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='name',
            field=models.CharField(default='N/A', max_length=25),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='date_of_birth',
            field=models.DateField(blank=True, default='N/A', null=True),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='national_id',
            field=models.CharField(default='N/A'),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='phone_number',
            field=models.CharField(blank=True, default='N/A', max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='user_type',
            field=models.CharField(default='N/A'),
        ),
    ]