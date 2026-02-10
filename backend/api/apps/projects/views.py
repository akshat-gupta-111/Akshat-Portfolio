from django.shortcuts import render
from .models import ProjectCard


# Create your views here.
def index(request):
    cards = ProjectCard.objects.order_by("title")
    data = {
        "card_list": cards,
    }
    return render(request, "projects/index.html", data)
