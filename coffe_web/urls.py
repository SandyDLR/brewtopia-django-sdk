from django.urls import path, include, re_path
from . import views

urlpatterns = [
    path("", views.starting_page, name="starting-page"),
    path('i18n/', views.starting_page),
]