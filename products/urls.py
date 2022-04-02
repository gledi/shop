from django.urls import path

from products import views


urlpatterns = [
    path("", views.get_products, name="product_list"),
    path("add/", views.add_product, name="product_add"),
    path("alt/", views.ProductListView.as_view(), name="product_list_alt"),
    path("<int:pk>/", views.get_product_details, name="product_details"),
    path(
        "<int:id>/alt/",
        views.ProductDetailView.as_view(),
        name="product_details_alt",
    ),
    path("<int:pk>/discount/", views.discount_product, name="discount_product"),
    path("latest/", views.get_latest_offers, name="latest_offers"),
    path("dump/", views.dump_products, name="dump_products"),
]
