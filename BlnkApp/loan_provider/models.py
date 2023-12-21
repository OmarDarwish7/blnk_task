from django.db import models
from users.models import UserModel
# Create your models here.
class LoanProviderModel(models.Model):
    id = models.OneToOneField(UserModel, primary_key=True, on_delete=models.CASCADE)
    current_total_funds = models.FloatField()