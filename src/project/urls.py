"""
    All project URLs.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Admin panel.
    path("admin/", admin.site.urls, name="admin"),
    # Shop URLs (Actual app).
    path("", include("shop.urls"), name="shop"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_URL)

if settings.URL_PREFIX:
    # If there is a URL prefix, add to all.
    # Used for being behind a proxy / url prefix.
    urlpatterns = [path(f"{settings.URL_PREFIX}/", include(urlpatterns))]
