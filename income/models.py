from django.db import models
from accounts.models import Account

class Income(models.Model):
  account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='income_list', null=True)
  title = models.CharField(max_length=255)
  created_at = models.DateTimeField(auto_now_add=True)
  amount = models.FloatField(default=0)

  def __str__(self):
    return f'{self.account} - {self.amount} - {self.created_at}'