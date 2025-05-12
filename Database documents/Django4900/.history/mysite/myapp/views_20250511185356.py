from django.shortcuts import render, HttpResponse
from .models import County
from .models import School
from .models import Pathways

# Create your views here.
def home(request):
    countyList = County.objects.all().values('name')
    schoolList = School.objects.all().values('name')
    cNames = list(countyList)
    sNames = list(schoolList)
    return render(request, "base.html", {"cNames": cNames, "sNames": sNames})

def counties(request):
    items = County.objects.all()
    return render(request, "list.html", {"names": items})

def county(request):
    return render(request, "home.html")

def searchCounty(request, county_name=None):
    county = County.objects.filter(name=county_name).first()
    if county:
        return render(request, "King's County.html", {"county_name": county_name})
    else:
        return HttpResponse(f"No County found with the name {county_name}")

def searchSchool(request, school_name=None):
    school = School.objects.filter(name=school_name).first()
    if school:
        return render(request, "Brooklyn College.html", {"school": school})
    else:
        return HttpResponse(f"No School found with the name {school_name}")

def schools(request):
    schoolList = School.objects.all()
    return render(request, "list2.html", {"names": schoolList})

def pathways(request):
    pathwaysList = Pathways.objects.all()
    return render(request, "list3.html", {"names": pathwaysList})

def brooklynCollege(request):
    return render(request, "BrooklynCollege.html")

def kings(request):
    return render(request, "King's County.html")
