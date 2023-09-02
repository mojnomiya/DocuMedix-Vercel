from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from .forms import DoctorRegistrationForm, DoctorLoginForm
from doctor.models import Doctor

# Create your views here.

def doctor_register(request):
    if request.method == 'POST':
        form = DoctorRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            doctor = Doctor(doctor_account=user)
            doctor.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = DoctorRegistrationForm()
    
    context = {'form': form}
    return render(request, 'accounts/register.html', context)

def doctor_login(request):
    if request.method == 'POST':
        form = DoctorLoginForm(data=request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
    else:
        form = DoctorLoginForm()

    context = {'form': form}
    return render(request, 'accounts/login.html', context)

def doctor_logout(request):
    logout(request)
    return redirect('home')