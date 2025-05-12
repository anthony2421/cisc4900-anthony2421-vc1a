from django.shortcuts import render, HttpResponse
from .models import County

# Create your views here.
def home(request):
    return render(request, "base.html")

def counties(request):
    items = County.objects.all()
    return render(request, "list.html", {"names": items})