from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("app/new/", views.app_create, name="app_create"),
    path("app/edit/<int:pk>/", views.app_update, name="app_update"),
    path("app/delete/<int:pk>/", views.app_delete, name="app_delete"),
]