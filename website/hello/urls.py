from django.urls import path
from . import views
from .views import ListViews

urlpatterns = [
    path("login/", views.authFunc, name="authFunc"),
    path("welcomePage/", views.first_page, name="welcomePage"),
    path("workPermit/", views.work_permit, name="workPermit"),
    path("currentPermit/", views.lists, name="currentPermit"),
    path("docsSign/", views.docx_sign, name="docsSign"),
    path("workPermit/postDirector/", views.postDirector),
    path("workPermit/postManager/", views.postManager),
    path("workPermit/postExecutor/", views.postExecutor),
    path("workPermit/postWorker/", views.postWorker),
    path("workPermit/postStateEngineer/", views.postStateEngineer),
    path("workPermit/postShiftManager/", views.postShiftManager),
    path("workPermit/resultWorkPermit/", views.resultPermit, name="resultPermit"),

    path("firePermit/", views.firePermit, name="firePermit"),
    # path("firePermit/postDirector", views)
]