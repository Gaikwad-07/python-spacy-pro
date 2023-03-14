from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.login,name="login"),
    path('sign_in',views.sign_in,name="sign_in"),
    path('home',views.home,name="home"),
    path('add',views.add,name="add"),
    path('sign_up',views.sign_up, name="sign_up"),
    path('update/<int:id>',views.update, name="update" ),
    path('delete/<int:id>',views.delete, name="delete"),
    path('update/uprecord/<int:id>',views.uprecord, name="uprecord"),

]   