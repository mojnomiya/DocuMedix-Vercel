from datetime import date
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from .models import Doctor

from django import forms
from django.utils import timezone
from .models import Doctor
from .constants import GENDER_CHOICES

class DoctorProfileForm(forms.ModelForm):
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    class Meta:
        model = Doctor
        fields = ['age', 'date_of_birth', 'phone_no', 'gender', 'address', 'details', 'image', 'specialization', 'experience']

        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date', 'value': '1990-01-01'}),
            'details': forms.Textarea(attrs={'style': 'height: 100px;'}),
            'address': forms.Textarea(attrs={'style': 'height: 100px;'}),
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        placeholders = {
            'age': 33,
            'date_of_birth': 'Date of Birth',
            'phone_no': 'Phone No',
            'details': 'Details',
            'specialization': 'Ex - Cardiology',
            'experience': '10 Years'
        }
        
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'placeholder': placeholders.get(field)
            })


class UserEditForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['email','first_name', 'last_name']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        placeholders = {
            'email': 'Email',
            'first_name': 'First Name',
            'last_name': 'Last Name',
        }
        
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'placeholder': placeholders.get(field)
            })