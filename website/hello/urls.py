from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("welcomePage", views.first_page, name="firstPage"),
    path("workPermit", views.work_permit, name = "workPermit")
]