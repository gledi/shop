from django.urls import path

from pages import views


urlpatterns = [
    path("", views.home, name='home'),
    path("about/", views.about, name="about"),
    path("contact-us/", views.contact, name="contact"),
    path("privacy-policy/", views.privacy_policy, name="privacy")
]
