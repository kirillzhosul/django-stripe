from django.http import HttpResponse, JsonResponse, Http404
from django.shortcuts import render
from django.conf import settings
import stripe
from shop.models import Item


def item(req, item_id: int) -> HttpResponse:
    """
    Item page with information about and buy button.
    """
    item = Item.objects.get(pk=item_id)
    if not item:
        return Http404("Item does not exist!")

    # buy_fetch_endpoint -> where to send request to get Stripe session.
    # stripe_api_pk -> publishable key for Stripe API.
    buy_fetch_endpoint = (
        f"{'/' if settings.URL_PREFIX else ''}{settings.URL_PREFIX}/buy/{item_id}"
    )
    context = {
        "item_id": item_id,
        "item": item,
        "buy_fetch_endpoint": buy_fetch_endpoint,
        "stripe_api_pk": settings.STRIPE_API_PUBLISHABLE_KEY,
    }
    return render(req, "item.html", context)


def buy(req, item_id: int) -> JsonResponse:
    """
    Buy API method,
    returns Stripe session information,
    Item page fetches this method when user clicks `buy` button.
    Then client site (JS) redirects by Stripe SDK to payment screen.
    """
    item = Item.objects.get(pk=item_id)
    if not item:
        return Http404("Item does not exist!")

    stripe.api_key = settings.STRIPE_API_SECRET_KEY
    stripe_session = stripe.checkout.Session.create(
        line_items=[
            {
                "price_data": {
                    "currency": "usd",
                    "product_data": {
                        "name": f"{item.name} (Item №{item_id})",
                    },
                    "unit_amount": item.price,
                },
                "quantity": 1,
            }
        ],
        # Temporary for no env support!
        success_url=f"https://kirillzhosul.site/tests/stripe/item/{item_id}",
        cancel_url=f"https://kirillzhosul.site/tests/stripe/item/{item_id}",
        mode="payment",
    )
    return JsonResponse(
        {
            "success": {
                "item": {"id": item_id},
                "stripe_session": {"id": stripe_session.stripe_id},
            },
        }
    )


def index(req) -> HttpResponse:
    """
    Index root page.
    Simple template.
    """
    return render(req, "index.html", context={})
