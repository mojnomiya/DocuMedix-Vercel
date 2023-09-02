from datetime import date
from django.db import models
from doctor.constants import GENDER_CHOICES
from doctor.models import Doctor, Department

class PatientDetails(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    date_of_birth = models.DateField(null=True, blank=True)
    age = models.IntegerField()
    phone_no = models.CharField(max_length=14, null=True, blank=True)
    email = models.EmailField(blank=True, null=True)
    gender = models.CharField(max_length=32, choices=GENDER_CHOICES, null=True, blank=True)
    address = models.TextField(max_length=250, null=True, blank=True)
    image = models.ImageField(upload_to='photos/patients', null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    treating_doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)

    def get_full_name(self):
        return self.first_name + ' ' + self.last_name
    
    def __str__(self) -> str:
        return self.get_full_name()
    
    # def save(self, *args, **kwargs):
    #     if self.date_of_birth:
    #         today = date.today()
    #         age = today.year - self.date_of_birth.year - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))
    #         self.age = age
    #     super().save(*args, **kwargs)
    
