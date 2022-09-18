from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls, name="admin"),
    path("", include("shop.urls"), name="shop"),
]

if settings.URL_PREFIX:
    # If there is a URL prefix, add to all.
    urlpatterns = [path(f"{settings.URL_PREFIX}/", include(urlpatterns))]
