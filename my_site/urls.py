from django.urls import path, include
from . import views
''' link url patterns to the views.py program'''
urlpatterns = [
    path('', views.index),
]