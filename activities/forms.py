from django import forms
from .models import *

class WeeklyStudiesForm(forms.ModelForm):
  class Meta:
    model = WeeklyStudies
    fields = '__all__'

class FeedbacksForm(forms.ModelForm):
  class Meta:
    model = Feedbacks
    fields = ['content']
    labels  = {
      'content':'피드백 내용',
    }