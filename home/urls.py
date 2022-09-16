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
    path('sentmail/', views.sentmail, name = 'sentmail'),
    path('mails/<int:pk>/<int:sent>/', views.mail, name = 'mailopen'),
    path('sendmail/<int:pk>/', views.reply, name = 'mailreply'),
    path('mails/delete/<int:pk>/<int:sent>/', views.delete, name = 'maildelete'),
    path('mails/deletex/<int:pk>/<int:sent>/', views.deletex, name = 'maildeletex'),
]
