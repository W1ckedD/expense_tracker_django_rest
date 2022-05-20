from django.db import models
from accounts.models import Account

class Purchase(models.Model):
  account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='purchase_list')
  title = models.CharField(max_length=100)
  total_price = models.FloatField(default=0)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f'{self.account.user} - {self.title} -{self.total_price} - {self.created_at}'


class PurchaseItem(models.Model):
  purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE, related_name='items')
  title = models.CharField(max_length=100)
  quantity = models.IntegerField(default=1)
  price = models.FloatField(default=0)

  def __str__(self):
    return f'{self.title} --- {self.purchase}'