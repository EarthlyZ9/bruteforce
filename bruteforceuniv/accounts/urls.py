from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path(
        "signup/usernameavailability",
        views.username_availability,
        name="username-availability",
    ),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="accounts/login.html"),
        name="login",
    ),
    path("login/find_id/", views.find_id, name="find-id"),
    path("login/reset_password/", views.reset_password, name="reset-password"),
    path("check/login", views.check_login, name="check-login"),
    path("profile/", views.profile, name="profile"),
    path("profile/purchase_records", views.purchase_records, name="purchase-records"),
    path("profile/update_user_info", views.update_user_info, name="update-user-info"),
    path("profile/update_password", views.update_password, name="update-password"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("my_study_group/", views.my_study_group, name="my-study-group"),
]
