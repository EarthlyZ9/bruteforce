from django.urls import path
from . import views

urlpatterns = [
  path('', views.points, name='points-page'),
  path('points_info/', views.points_info, name='points-info'),
]
