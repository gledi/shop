from django.urls import path

from blog import views


app_name = "blog"

urlpatterns = [
    path("", views.get_post_list, name="post_list"),
    path("<slug:slug>", views.get_post_details, name="post_details"),
]
