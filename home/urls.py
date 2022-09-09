from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('about/', views.about, name = 'about'),
    path('contact/', views.contact, name = 'contact'),
    path('login/', views.loginUser, name = 'login'),
    path('logout/', views.logoutUser, name = 'logout'),
    path('signup/', views.signup, name = 'signup'),
    path('sendmail/', views.sendmail, name = 'sendmail'),
    path('mails/', views.mails, name = 'mails'),
    path('mails/<int:pk>/', views.mail, name = 'mailopen'),
    path('sendmail/<int:pk>/', views.reply, name = 'mailreply'),
    path('mails/delete/<int:pk>/', views.delete, name = 'maildelete'),
]
