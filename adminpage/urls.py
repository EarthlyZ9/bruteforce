from django.urls import path
from .views import base_views, python_views, ds_views, htmlcss_views

urlpatterns = [
    #base_views.py
    path('', base_views.admin_page, name='admin-page'),
    path('user_info/', base_views.user_info, name='user-info'),
    path('weekly_studies/', base_views.weekly_studies, name='weekly-studies'),
    path('python_points/', python_views.python_points, name='python-points'),
    path('ds_points', ds_views.ds_points, name='ds-points'),
    path('htmlcss_points', htmlcss_views.htmlcss_points, name='htmlcss-points'),
]