from django.shortcuts import render
from .models import SiteSettings
# Create your views here.
def index(request):
    setting = SiteSettings.objects.first()
    data = {
        "site" : setting,
    }
    return render(request, "home/index.html", data)