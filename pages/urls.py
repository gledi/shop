from django.urls import path

from pages import views


urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("pages/<page_name>/", views.PageView.as_view(), name="page"),
]
