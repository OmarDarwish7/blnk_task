from django.db import models
from users.models import UserModel


# Create your models here.
# Create your models here.
class LoanModel(models.Model):
    # Other fields related to the loan
    requested_amount = models.DecimalField(max_digits=10, decimal_places=2)
    interest_rate = models.FloatField()
    amount_after_interest = models.FloatField()
    amount_paid = models.FloatField()
    amount_to_pay = models.FloatField()
    monthly_amount = models.FloatField()
    bank_percentage = models.FloatField()
    term = models.IntegerField()
    status = models.CharField()

    # Foreign key referencing the custom UserModel
    customer = models.ForeignKey(UserModel, on_delete=models.CASCADE,related_name = 'loan_customer')
