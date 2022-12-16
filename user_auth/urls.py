from django.contrib import admin
from django.urls import path, include
from django.urls import path, include, re_path
from . import views

'''App to authenticate users on the site,
create url patters to login and then authenticaiton
'''

app_name = 'user_auth'

urlpatterns = [
    path('', views.user_login, name='login'),
    path('authenticate_user/', views.authenticate_user,
name='authenticate_user')
]