from django.db import models

# Create your models here.
class LoanSchemaModel(models.Model):
    min_amount = models.FloatField()
    max_amount = models.FloatField()
    interest_rate = models.FloatField()
    term = models.IntegerField()
    bank_percentage = models.FloatField()