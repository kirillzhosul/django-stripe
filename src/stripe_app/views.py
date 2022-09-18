from django.http import HttpResponse
from django.urls import path


def item(req) -> HttpResponse:
    return HttpResponse("item view")


def buy(req) -> HttpResponse:
    return HttpResponse("buy view")


def index(req) -> HttpResponse:
    return HttpResponse("index view")
