from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'hello/authorization/index.html')

def first_page(request):
    return render(request, 'hello/firstPage/firstPage.html')

def work_permit(request):
    return render(request, 'hello/workPermit/workPermit.html')

