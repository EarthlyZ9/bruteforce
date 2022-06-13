from django import forms
from .models import ProgressPointsFile, StudyGroupAssign


class ProgressPointsFileForm(forms.ModelForm):
    class Meta:
        model = ProgressPointsFile
        fields = "__all__"


class StudyGroupAssignForm(forms.ModelForm):
    class Meta:
        model = StudyGroupAssign
        fields = "__all__"
