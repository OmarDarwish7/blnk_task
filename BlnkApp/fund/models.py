from django.db import models
from loan_provider.models import LoanProviderModel
from loan_provider.models import LoanProviderModel


# Create your models here.
# Create your models here.
class FundModel(models.Model):
    # Other fields related to the loan
    amount = models.BigIntegerField()
    date = models.DateField()
    # Foreign key referencing the custom UserModel
    provider = models.ForeignKey(LoanProviderModel, on_delete=models.CASCADE,related_name = 'loan_provider')
