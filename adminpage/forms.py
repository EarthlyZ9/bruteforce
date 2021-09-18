from django import forms
from .models import ProgressPointsFile

class ProgressPointsFileForm(forms.ModelForm):
  class Meta:
    model = ProgressPointsFile
    fields = '__all__'