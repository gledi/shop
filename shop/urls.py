from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from products.views import get_user_products

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("pages.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("products/", include("products.urls")),
    path("posts/", include("blog.urls")),
    path("users/<username>/products/", get_user_products, name="user_products"),
    path("api/v1/", include("apiv1.urls")),
    path("api/v2/", include("apiv2.urls")),
    path("__debug__/", include("debug_toolbar.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
