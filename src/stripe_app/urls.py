from django.contrib import admin
from django.urls import path, include
from django.conf import settings

from stripe_app import views

urlpatterns = [
    path("admin/", admin.site.urls, name="admin"),
    path(
        "buy/<int:item_id>",
        views.buy,
        name="buy",
    ),
    path(
        "item/<int:item_id>",
        views.item,
        name="item",
    ),
    path("", views.index, name="index"),
]
if settings.URL_PREFIX:
    # If there is a URL prefix, add to all.
    urlpatterns = [path(f"{settings.URL_PREFIX}/", include(urlpatterns))]
