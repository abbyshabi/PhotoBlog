from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404
import datetime as dt
from .models import Image,Category,Location
# Create your views here.

def photos(request):
    images = Image.get_photos()
    return render(request,'index.html',{"images":images})
