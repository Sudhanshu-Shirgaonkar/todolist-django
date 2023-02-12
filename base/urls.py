
from django.contrib import admin
from django.urls import path

from .import views

urlpatterns = [
    path("", views.index,name='index'),
    path("delete/<str:pk>",views.delete,name='delete'),
    path("update/<str:pk>",views.update,name='update'),
    path("login/",views.userLogin,name='login'),
    path("register/",views.register, name="register"),
    path("logout",views.logoutUser, name="logout"),

    
]
