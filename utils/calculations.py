def calculate_current_balance(request):
  _sum = 0
  income_list = request.user.account.income_list.all()
  for income in income_list:
    _sum += income.amount
  
  purchase_list = request.user.account.purchase_list.all()
  for purchase in purchase_list:
    _sum -= purchase.total_price

  return _sum

def calculate_purchase_total_price(purchase):
  _sum = 0
  purchase_list_items = purchase.items.all()

  for item in purchase_list_items:
    _sum += item.price * item.quantity

  return _sum