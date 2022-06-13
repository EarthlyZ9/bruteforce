from adminpage.models import AdditionalPoints, WeeklyActivityPoints
from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(WeeklyActivityPoints)
admin.site.register(Progress)
admin.site.register(AdditionalPoints)
admin.site.register(PointsStatus)
admin.site.register(ProgressPointsFile)
admin.site.register(StudyGroupAssign)
