from django.db import models
from accounts.models import Account_Info
#from activities.models import Activities

# Create your models here.
class Points_purchase(models.Model):
  name = models.CharField(max_length=100)
  num = models.IntegerField(primary_key=True)
  price = models.IntegerField()
  description = models.TextField()
  img_path = models.CharField(max_length=225)
  #가용 포인트

  def __str__(self):
    return self.name

class PurchaseRequest(models.Model):
  user = models.ForeignKey(Account_Info, on_delete=models.CASCADE)
  purchase_option = models.ForeignKey(Points_purchase, on_delete=models.CASCADE)
  purchase_datetime = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return str(self.user) + '_' + str(self.purchase_datetime)

