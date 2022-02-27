from django.urls import path

from products import views


urlpatterns = [
    path("", views.get_products, name="product_list"),
    path("alt/", views.ProductListView.as_view(), name="product_list_alt"),
    path("<int:pk>/", views.get_product_details, name="product_details"),
]
