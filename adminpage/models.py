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


def make_file_path(instance, filename):
  path = 'progress_studies/{season}/{filename}'.format(
    season=instance.week.season,
    filename=filename,
  )
  return path

class ProgressPointsFile(models.Model):
  PERIOD_CHOICES = (
    ('1', '1차 진도율'),
    ('2', '2차 진도율'),
    ('3', '3차 진도율'),
    ('final', '최종 진도율'),
    ('completion', '종료 시점 진도율 (수료증)'),
  )
  period = models.CharField(max_length=20, choices=PERIOD_CHOICES)
  file = models.FileField(upload_to=make_file_path)
  