from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.conf import settings


def item(req, item_id: int) -> HttpResponse:
    """
    Item page with information about and buy button.
    """
    # buy_fetch_endpoint -> where to send request to get Stripe session.
    # stripe_api_pk -> publishable key for Stripe API.
    context = {
        "item_id": item_id,
        "buy_fetch_endpoint": f"/{settings.URL_PREFIX}/buy/{item_id}",
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
    stripe_session_id = "test"
    return JsonResponse(
        {
            "success": {
                "item": {"id": item_id},
                "stripe_session": {"id": stripe_session_id},
            },
        }
    )


def index(req) -> HttpResponse:
    """
    Index root page.
    Simple template.
    """
    return render(req, "index.html", context={})
