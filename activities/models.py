from django.db import models
from accounts.models import Account_Info
import os


# Create your models here.
class Material(models.Model):
  CATEGORY = (
    ('common', '공통'),
    ('python', '파이썬'),
    ('datascience', '데이터 사이언스'),
    ('htmlcss', '웹 퍼블리싱')
  )

  
  title = models.CharField(max_length=225)
  file_type = models.CharField(max_length=50)
  open_week = models.IntegerField(blank=True, null=True)
  content = models.TextField()
  category = models.CharField(max_length=20, choices=CATEGORY)
  file = models.FileField(upload_to="materials/%Y/%m/%d", null=True, blank=True)
  upload_date = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.title
  
  def get_filename(self):
    return os.path.basename(self.file.name)


def make_file_path(instance, filename):
  path = 'weekly_studies/{season}/{username}/{filename}'.format(
    season=instance.week.season,
    username= instance.user.name,
    filename=filename,
  )
  return path


class WeeklyStudies(models.Model):
  user = models.ForeignKey(Account_Info, on_delete=models.CASCADE)
  week = models.ForeignKey('Week', on_delete=models.CASCADE)
  attendance = models.TextField(null=True, blank=True)
  file = models.FileField(upload_to=make_file_path, null=True, blank=True)
  url = models.URLField(max_length=300, null=True, blank=True)
  submit_date = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return str(self.user) + "_" + str(self.week)

  class Meta:
    unique_together = (("user","week"),)


class Week(models.Model):
  season = models.IntegerField()
  week_num = models.IntegerField()
  start_date = models.DateField()
  end_date = models.DateField()

  class Meta:
    unique_together = (("season", "week_num"),)

  def __str__(self):
    return str(self.week_num)

class HtmlFruits(models.Model):
  TOPIC = (
    ('Semi1', '세미 프로젝트 1'),
    ('Semi2', '세미 프로젝트 2'),
    ('Semi3', '세미 프로젝트 3'),
    ('Final', '파이널 프로젝트')
  )
  author = models.ForeignKey(Account_Info, on_delete=models.CASCADE, related_name='author_htmlfruits')
  topic = models.CharField(max_length=40, choices=TOPIC)
  url = models.URLField(max_length=300)
  create_date = models.DateTimeField(auto_now_add=True)
  voter = models.ManyToManyField(Account_Info, related_name='voter_htmlfruits')

  def __str__(self):
    return str(self.author) + '_' + str(self.topic)

class Feedbacks(models.Model):
  author = models.ForeignKey(Account_Info, on_delete=models.CASCADE)
  content = models.TextField()
  create_date = models.DateTimeField(auto_now_add=True)
  feedback_to = models.ForeignKey(HtmlFruits, on_delete=models.CASCADE)

  def __str__(self):
    return str(self.author)+ "'s feedback_to " + str(self.feedback_to) 
