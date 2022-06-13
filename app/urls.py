from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from . import views
from app.views import *


app_name = 'app'


urlpatterns = [
    path('',dashboard,name='dashboard'),
    path('admin_dashboard',admin_dashboard,name='admin_dashboard'),
    path('quiz',quiz,name='quiz'),
    path("register", views.register_request, name="register"),
    path("login", views.login_request, name="login"),
    path("logout", views.logout_request, name= "logout"),
    path("category_filter", views.category_filter, name= "category_filter"),
]