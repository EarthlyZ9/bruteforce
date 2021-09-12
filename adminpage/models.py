from django.db import models
from accounts.models import Account_Info

class WeeklyActivityPoints(models.Model):
  week_num =  models.IntegerField()
  user = models.ForeignKey(Account_Info, on_delete=models.CASCADE)
  attendance = models.IntegerField(null=True, blank=True, default=0)
  weekly_studies = models.IntegerField(null=True, blank=True, default=0)
  

  def __str__(self):
    return str(self.user) + '_' + str(self.week_num)

class Progress(models.Model):
  user = models.ForeignKey(Account_Info, on_delete=models.CASCADE)
  progress1 = models.IntegerField(null=True, blank=True, default=0)
  progress2 = models.IntegerField(null=True, blank=True, default=0)
  progress3 = models.IntegerField(null=True, blank=True, default=0)
  progress4 = models.IntegerField(null=True, blank=True, default=0)

  def __str__(self):
    return str(self.user)

class AdditionalPoints(models.Model):
  user = models.ForeignKey(Account_Info, on_delete=models.CASCADE)
  additional_points = models.IntegerField(null=True, blank=True, default=0)

  def __str__(self):
    return str(self.user)

#누적 포인트와 사용포인트 
class PointsStatus(models.Model):
  user = models.ForeignKey(Account_Info, on_delete=models.CASCADE)
  total_points = models.IntegerField(null=True, blank=True, default=0)
  used_points = models.IntegerField(null=True, blank=True, default=0)

  def __str__(self):
    return str(self.user)