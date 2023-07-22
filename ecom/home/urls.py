from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.home,name="home"),
    path('loginuser', views.loginuser,name="loginuser"),
    path('logoutuser', views.logoutuser,name="logoutuser"),
    path('register', views.register,name="register"),
    path('userpage', views.userpage,name="userpage"),
    path('userprofile', views.userprofile,name="userprofile"),
   
    

    path('product',views.product,name="product"),
    path('createorder/<str:pk>/',views.createOrder,name="createorder"),
    path('customer/<str:pk_test>/',views.customer,name="customer"),


    path('updateorder/<str:pk>/',views.updateOrder,name="updateorder"),
    path('deleteorder/<str:pk>/',views.deleteOrder,name="deleteorder"),
    path('updatecustomer/<str:pk>/',views.updatecustomer,name="updatecustomer"),
    path('deletecustomer/<str:pk>/',views.deletecustomer,name="deletecustomer"),
]