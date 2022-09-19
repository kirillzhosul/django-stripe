"""
    Shop URLs.
"""
from django.urls import path

from shop import views

urlpatterns = [
    # Index view.
    path("", views.index_view, name="index"),
    # Buy view, that returns Stripe session.
    path(
        "buy/<int:item_id>",
        views.buy_view,
        name="buy",
    ),
    # Item view, that returns page with item information or 404.
    path(
        "item/<int:item_id>",
        views.item_view,
        name="item",
    ),
]
