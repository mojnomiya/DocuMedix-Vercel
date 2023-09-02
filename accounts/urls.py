from django.urls import path
from accounts import views

urlpatterns = [
    path('login/', views.doctor_login, name='login'),
    path('register/', views.doctor_register, name='register'),
    path('logout/', views.doctor_logout, name='logout'),
]