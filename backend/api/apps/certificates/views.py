from django.shortcuts import render
from .models import CertificateCard


# Create your views here.
def index(request):
    cards = CertificateCard.objects.filter(is_available=True).order_by("title")
    data = {
        "card_list": cards,
    }
    return render(request, "certificates/index.html", data)
