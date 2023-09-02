from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import DoctorProfileForm, UserEditForm
from patient.models import PatientDetails
from .models import Doctor

@login_required
def edit_doctor_profile(request):
    doctor = request.user.doctor
    alert = ''
    if request.method == 'POST':
        doctor_form = DoctorProfileForm(request.POST, request.FILES, instance=doctor)
        user_form = UserEditForm(request.POST, instance=request.user)

        if doctor_form.is_valid() and user_form.is_valid():
            doctor_form.save()
            user_form.save()
            alert = 'successfull'
            return redirect('profile')
        else:
            alert = 'unsuccessfull'
    else:
        doctor_form = DoctorProfileForm(instance=doctor)
        user_form = UserEditForm(instance=request.user)

    return render(request, 'doctor/edit-doctor.html', {'doctor_form': doctor_form, 'user_form': user_form})


@login_required
def dashboard(request):
    if request.user.is_authenticated:
        doctor = request.user.doctor
        patients = PatientDetails.objects.filter(treating_doctor=doctor)

        return render(request, 'doctor/dashboard.html', {'patients': patients})
    else:
        return render(request, 'login.html')
    
@login_required
def profile(request):
    if request.user.is_authenticated:
        doctor = request.user.doctor
        # patients = doctor.patient_set.all()
        # appointments = doctor.appointment_set.all()
        return render(request, 'doctor/about-doctor.html', {'doctor': doctor})
    else:
        return redirect('login')
    
    