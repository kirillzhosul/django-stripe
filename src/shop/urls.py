"""
    Shop URLs.
"""
from django.urls import path

from shop import views

urlpatterns = [
    # Index view.
    path("", views.index_view, name="index"),
    # Payment end views.
    path("/finish/success", views.payment_success_view, name="payment_success"),
    path("/finish/failed", views.payment_failed_view, name="payment_failed"),
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
