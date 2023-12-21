from django.db import models
from loan.models import LoanModel
from users.models import UserModel
from loan_provider.models import LoanProviderModel
# Create your models here.
class SubloanModel(models.Model):
    share_of_total = models.FloatField()
    monthly_amount = models.FloatField()
    total_amount = models.FloatField()
    current_paid = models.FloatField(default =0.0)
    amount_to_pay = models.FloatField(default = 0.0)
    

    #Foreign Keys
    loan = models.ForeignKey(LoanModel, on_delete = models.CASCADE, related_name = 'loan_id')
    customer = models.ForeignKey(UserModel, on_delete=models.CASCADE,related_name = 'customer_id')
    provider = models.ForeignKey(LoanProviderModel,on_delete=models.CASCADE,related_name = 'provider_id')