from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'hello/authorization/index.html')

def first_page(request):
    values = {"count": 5}
    return render(request, 'hello/firstPage/firstPage.html', values)

def work_permit(request):
    return render(request, 'hello/workPermit/workPermit.html')

def current_permit(request):
    return render(request, 'hello/currentWorkPermits/currentWork.html')
