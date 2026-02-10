from django.shortcuts import render
from .models import SocialCard

# Create your views here.
from django.http import HttpResponse


def index(request):
    cards = SocialCard.objects.filter(is_available=True).order_by("title")
    data = {
        "card_list": cards,
    }

    return render(request, "socials/index.html", data)
