from django.db import models
from django.contrib.auth.models import User

class Account(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='account', null=True)
  current_balance = models.FloatField(default=0)