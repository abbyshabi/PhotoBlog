from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404
import datetime as dt
from .models import Image,Category,Location
# Create your views here.

def photos(request):
    images = Image.get_photos()
    return render(request,'index.html',{"images":images})

def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        category = request.GET.get("image")
        searched_images = Image.search_by_category(category)
        message = f"{category}"

        return render(request, 'search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any image"
        return render(request, 'search.html',{"message":message})    
