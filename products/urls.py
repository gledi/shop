from django.urls import path

from products import views


urlpatterns = [
    path("", views.get_products, name="product_list"),
    path("<int:pk>/", views.get_product_details, name="product_details"),
    path("<int:pk>/review/", views.review_product, name="review_product"),
]
