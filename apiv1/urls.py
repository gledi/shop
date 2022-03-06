from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from apiv1 import views


app_name = "apiv1"

urlpatterns = [
    path("categories/", views.category_list, name="category_list"),
    path("categories/<int:pk>/", views.category_details, name="category_details"),
    path("products/", views.ProductListView.as_view(), name="product_list"),
    path("products/<int:pk>/", views.ProductView.as_view(), name="product_details"),
]

urlpatterns = format_suffix_patterns(urlpatterns, allowed=["json", "xml", "html"])
