from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from patient.forms import AddPatientForm
from .models import PatientDetails
from doctor.models import Department

# Create your views here.
# def add_patient(request):
    # if request.method == 'POST':
    #     form = AddPatientForm(request.POST, request.FILES)
    #     print(form.is_valid())
    #     print(form.errors)
    #     if form.is_valid():
    #         new_patient = form.save(commit=False)
    #         if request.user.is_authenticated:
    #             doctor = request.user.doctor
    #             new_patient.treating_doctor = doctor
    #             new_patient.save()
    #         return redirect('dashboard')
    # else:
    #     form = AddPatientForm()
    # return render(request, 'patient/add-patient.html', {'form': form})

@login_required
def add_patient(request):
    if request.method == 'POST':
        form = AddPatientForm(request.POST, request.FILES)
        
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        date_of_birth = request.POST.get('date_of_birth')
        age = request.POST.get('age')
        phone_no = request.POST['phone_no']
        email = request.POST['email']
        gender = request.POST['gender']
        department_entered = request.POST.get('department')
        if department_entered == '':
            department_entered = 10
        department = Department.objects.get(id=department_entered)

        address = request.POST['address']
        image = request.POST.get('image')
        print(image)
        new_patient = PatientDetails(
            first_name=first_name,
            last_name=last_name,
            date_of_birth=date_of_birth,
            age=age,
            phone_no=phone_no,
            email=email,
            gender=gender,
            department=department,

            address=address,
            image=image
        )

        if request.user.is_authenticated:
            doctor = request.user.doctor
            new_patient.treating_doctor = doctor

        new_patient.save()
        return redirect('dashboard')
    else:
        form = AddPatientForm()

    return render(request, 'patient/add-patient.html', {'form': form})



# def edit_patient_detail(request, patient_id):
#     patient = get_object_or_404(PatientDetails, pk=patient_id)

#     if request.method == 'POST':
#         form = AddPatientForm(request.POST, request.FILES, instance=patient)

#         if form.is_valid():
#             updated_patient = form.save(commit=False)
#             if request.user.is_authenticated:
#                 doctor = request.user.doctor
#                 updated_patient.treating_doctor = doctor
#             updated_patient.save()

#             return redirect('dashboard')
#     else:
#         form = AddPatientForm(instance=patient)

#     return render(request, 'patient/edit-patient.html', {'form': form})

@login_required
def edit_patient_detail(request, patient_id):
    patient = get_object_or_404(PatientDetails, pk=patient_id)

    if request.method == 'POST':
        form = AddPatientForm(request.POST, request.FILES)
        
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        date_of_birth = request.POST.get('date_of_birth')
        age = request.POST.get('age')
        phone_no = request.POST['phone_no']
        email = request.POST['email']
        gender = request.POST['gender']
        print(gender)
        department_entered = request.POST.get('department')
        if department_entered == '':
            department_entered = 10
        department = Department.objects.get(id=department_entered)

        address = request.POST['address']
        image = request.POST.get('image')

        patient.first_name = first_name
        patient.last_name = last_name
        patient.date_of_birth = date_of_birth
        patient.age = age
        patient.phone_no = phone_no
        patient.email = email
        patient.gender = gender
        patient.department = department
        patient.address = address
        patient.image = image

        if request.user.is_authenticated:
            doctor = request.user.doctor
            patient.treating_doctor = doctor

        patient.save()
        return redirect('dashboard')
    else:
        form = AddPatientForm(instance=patient)

    return render(request, 'patient/edit-patient.html', {'form': form})

@login_required
def delete_patient_detail(request, patient_id):
    patient = get_object_or_404(PatientDetails, pk=patient_id)
    patient.delete()
    return redirect('dashboard')


def search_patients(request):
    query = request.GET.get('q')
    if query:
        patients = PatientDetails.objects.filter(
            Q(first_name__icontains=query) | 
            Q(last_name__icontains=query) 
        )
    else:
        patients = PatientDetails.objects.all()

    return render(request, 'patient/search_results.html', {'patients': patients})


@login_required
def patient_detail(request, patient_id):
    patient = PatientDetails.objects.get(pk=patient_id)
    return render(request, 'patient/about-patient.html', {'patient': patient})