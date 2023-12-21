from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class UserModel(AbstractUser):
    # name = models.CharField(max_length=30)
    # date_of_birth = models.DateField()
    name = models.CharField(max_length = 25, default = "N/A")
    phone_number = models.CharField(max_length=15, blank=True, null=True, default = "N/A")
    date_of_birth = models.DateField(blank=True, null=True, default = "N/A")
    user_type = models.CharField(blank=False,null=False, default = "N/A")
    national_id = models.CharField(blank=False,null=False, default = "N/A")


    def __str__(self):
        return self.username