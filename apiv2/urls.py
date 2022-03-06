from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from apiv2 import views


app_name = "apiv2"

urlpatterns = [
    path("products/", views.ProductListView.as_view(), name="product_list"),
]

urlpatterns = format_suffix_patterns(urlpatterns, allowed=["json", "xml", "html"])
