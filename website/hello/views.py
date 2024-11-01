from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'hello/index.html')

def page(request):
    return render(request, 'hello/firstPage.html')