from django.shortcuts import render
from patient.models import PatientDetails
from doctor.models import Department

def home(request):
    patients = PatientDetails.objects.all()
    departments = Department.objects.all()
    if request.method == 'POST':
        selected_department = request.POST.get("category")

        if selected_department != "none":
            patients = PatientDetails.objects.filter(department__department_name=selected_department)
    return render(request, 'index.html', {'patients': patients, 'departments': departments})