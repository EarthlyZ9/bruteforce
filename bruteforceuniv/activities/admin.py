from django.contrib import admin
from .models import Feedbacks, HtmlFruits, Material, Week, WeeklyStudies

# Register your models here.
admin.site.register(Material)
admin.site.register(Week)
admin.site.register(WeeklyStudies)
admin.site.register(HtmlFruits)
admin.site.register(Feedbacks)