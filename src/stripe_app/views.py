from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.conf import settings


def item(req, item_id: int) -> HttpResponse:
    return render(
        req,
        "item.html",
        context={
            "item_id": item_id,
            "buy_fetch_endpoint": f"/{settings.URL_PREFIX}/buy/{item_id}",
            "stripe_api_pk": settings.STRIPE_API_PUBLISHABLE_KEY,
        },
    )


def buy(req, item_id: int) -> JsonResponse:
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
    return render(req, "index.html", context={})
