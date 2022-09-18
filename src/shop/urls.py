from django.urls import path

from shop import views

urlpatterns = [
    path("", views.index, name="index"),
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
]
