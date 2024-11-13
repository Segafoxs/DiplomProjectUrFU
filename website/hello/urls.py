from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("welcomePage/", views.first_page, name="welcomePage"),
    path("workPermit/", views.work_permit, name="workPermit"),
    path("currentPermit/", views.current_permit, name="currentPermit"),
    path("workPermit/postuser/", views.postuser),
]