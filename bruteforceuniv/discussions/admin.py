from discussions.models import Answer, Question
from django.contrib import admin
from .models import Question, Answer, Comment

# Register your models here.
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Comment)
