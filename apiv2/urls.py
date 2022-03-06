from django.urls import path

from apiv2 import views

app_name = "apiv2"

urlpatterns = [
    path("products/", views.ProductListView.as_view(), name="product_list"),
]
