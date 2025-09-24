from django.shortcuts import render
from django.http import HttpResponse
import math

def anyName(request):
    return render(request, "about.html")

def fact(request):
    result = None
    if request.method == "POST":
        Number = request.POST.get("Number")
        if Number:
            Number = int(Number)
            result = math.factorial(Number)
    return render(request, "about.html", {"result":result})

# Create your views here.
