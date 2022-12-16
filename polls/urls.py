from django.urls import path, include, re_path
from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.user_login, name='login'),
    path('authenticate_user/', views.authenticate_user,name='authenticate_user'),
    path('', views.index, name='index'),
    path("register", views.register_request, name="register"),
    path('<int:question_id>', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]