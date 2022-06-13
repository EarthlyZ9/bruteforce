from django.urls import path
from . import views

urlpatterns = [
  path('', views.main_page, name='main-page'),
  path('intro/about_us', views.about_us, name='about-us'),
  path('intro/course_description', views.course_description, name='course-description'),
  path('intro/program_description', views.program_description, name='program-description'),
  path('intro/program_description/python', views.python_description, name='python-description'),
  path('intro/program_description/data_science', views.ds_description, name='ds-description'),
  path('intro/program_description/web_publishing', views.htmlcss_description, name='htmlcss-description'),
  path('instagram/',views.instagram, name='instagram'),
  path('kakao_plus/',views.kakao_plus,  name='kakao-plus'),
]