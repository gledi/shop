from django.urls import path

from pages import views


urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("super-secret/", views.super_secret, name="secret"),
    path("pages/<page_name>/", views.PageView.as_view(), name="page"),
    path("policy-agreement/", views.policy_agreement, name="policy_agreement"),
    path("big-prize/", views.big_prize, name="big_prize"),
]
