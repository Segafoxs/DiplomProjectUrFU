from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.authFunc, name="authFunc"),
    path("welcomePage/", views.first_page, name="welcomePage"),

    path("workPermit/", views.work_permit, name="workPermit"),
    path("currentPermit/", views.current_permit, name="currentPermit"),
    path("workPermit/postDirector/", views.postDirector),
    path("workPermit/postManager/", views.postManager),
    path("workPermit/postExecutor/", views.postExecutor),
    path("workPermit/postShiftManager/", views.postShiftManager),
    path("workPermit/resultWorkPermit/", views.resultPermit, name="resultPermit"),

    path("firePermit/", views.firePermit, name="firePermit"),
    # path("firePermit/postDirector", views)
]