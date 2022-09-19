"""
    Views for API / templates.
"""

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.conf import settings
from shop.services.stripe import create_stripe_session
from shop.models import Item

# Non async!
def item_view(req, item_id: int) -> HttpResponse:
    """
    Item page with information about and buy button.
    """
    item = get_object_or_404(Item, pk=item_id)
    return render(
        req,
        "item.html",
        context={
            "item": item,
            "buy_fetch_endpoint": f"{'/' if settings.URL_PREFIX else ''}{settings.URL_PREFIX}/buy/{item_id}",
            "stripe_api_pk": settings.STRIPE_API_PUBLISHABLE_KEY,
        },
    )


# Non async!
def buy_view(_, item_id: int) -> JsonResponse:
    """
    Buy API method,
    returns Stripe session information,
    Item page fetches this method when user clicks `buy` button.
    Then client site (JS) redirects by Stripe SDK to payment screen.
    """
    item = get_object_or_404(Item, pk=item_id)
    stripe_session = create_stripe_session(
        secret_key=settings.STRIPE_API_SECRET_KEY,
        # Temporary!
        redirect_url="https://kirillzhosul.site/tests/stripe/",
        product_name=str(item),
        price=item.price,
        quantity=1,
        currency="usd",
    )
    return JsonResponse(
        {
            "success": {
                "item": {"id": item_id},
                "stripe_session": {"id": stripe_session.stripe_id},
            },
        }
    )


# Non async!
def index_view(req) -> HttpResponse:
    """
    Index root page. Simple template to display with list of items.
    """
    newest_items = Item.objects.order_by("-item_id")[:10]
    return render(req, "index.html", context={"newest_items": newest_items})
