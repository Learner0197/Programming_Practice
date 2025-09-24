from django.http import HttpResponse
from django.shortcuts import render
import math
def homepage(request):
    return HttpResponse("Hello, world...Home app/Page")

def bye(request):
    print(request.POST.get("username"))
    print(request.POST.get("password"))
    
    return HttpResponse("Bye Bye...")

# Create your views here.
