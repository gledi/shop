from django.urls import path

from accounts import views


urlpatterns = [
    path("managers/", views.manager_view, name="manager_view"),
    path("everyone/", views.everyone_view, name="everyone_view"),
]
