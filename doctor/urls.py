from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('edit-profile/', views.edit_doctor_profile, name='edit-profile'),
    path('dashboard/', views.dashboard, name='dashboard'),
]