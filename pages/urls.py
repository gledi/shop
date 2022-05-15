from django.urls import path

from pages import views


app_name = "pages"

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("languages/<language>/", views.switch_language, name="switch_language"),
    path("super-secret/", views.super_secret, name="secret"),
    path("pages/<page_name>/", views.PageView.as_view(), name="page"),
    path("policy-agreement/", views.policy_agreement, name="policy_agreement"),
    path("big-prize/", views.big_prize, name="big_prize"),
]
