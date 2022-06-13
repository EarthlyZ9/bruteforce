from django.urls import path
from . import views
from .views import FileDownLoadView

urlpatterns = [
    path("rankings/", views.rankings, name="rankings"),
    path("study_log/", views.study_log, name="study-log"),
    path("htmlcss_outputs/", views.htmlcss_fruits, name="htmlcss-fruits"),
    path(
        "htmlcss_outputs/create_feedback/<int:fruit_id>",
        views.create_feedback,
        name="create-feedback",
    ),  # feedback 등록하기
    path(
        "htmlcss_outputs/feedbacks/", views.load_feedbacks, name="htmlcss-feedbacks"
    ),  # feedback 보여주기
    path(
        "htmlcss_outputs/feedbacks/vote/<int:fruit_id>/",
        views.vote_fruit,
        name="vote-fruit",
    ),  # 추천
    path("weekly_studies/", views.weekly_studies, name="weekly-studies"),
    path("materials/", views.material_list, name="material-list"),
    path("materials/<int:pk>/", FileDownLoadView.as_view(), name="download"),
]
