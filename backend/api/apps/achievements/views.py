from django.shortcuts import render
from .models import Achievements


# Create your views here.
def index(request):
    cards = Achievements.objects.order_by("title")
    data = {
        "card_list": cards,
    }
    return render(request, "achievements/index.html", data)
