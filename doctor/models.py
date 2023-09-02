from django.db import models
from django.contrib.auth.models import User
from .constants import GENDER_CHOICES


class Department(models.Model):
    department_name = models.CharField(max_length=150)
    
    def __str__(self) -> str:
        return self.department_name


class Doctor(models.Model):
    doctor_account = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    age = models.IntegerField(null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    phone_no = models.CharField(max_length=14, null=True, blank=True)
    gender = models.CharField(max_length=32, choices=GENDER_CHOICES, null=True, blank=True)
    address = models.TextField(max_length=250, null=True, blank=True)
    details = models.TextField(max_length=500, null=True, blank=True)
    image = models.ImageField(upload_to='photos/doctors', null=True, blank=True)
    specialization = models.CharField(max_length=100, null=True, blank=True)
    experience = models.CharField(max_length=64, null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, blank=True, null= True)
    # patients = models.ManyToManyField(PatientDetails, related_name='treating_doctors')
    
    def __str__(self):
        if self.doctor_account:
            return self.doctor_account.get_full_name()
        else:
            return "Doctor ID: {}".format(self.pk)
        
