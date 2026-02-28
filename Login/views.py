from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.http import HttpResponse


def home(request):
    return render(request,'home.html',{"context":"Hi "})

