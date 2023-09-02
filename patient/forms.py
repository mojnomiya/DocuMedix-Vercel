from django import forms
from .models import PatientDetails

class AddPatientForm(forms.ModelForm):
    
    class Meta:
        model = PatientDetails
        fields = ['first_name', 'last_name', 'date_of_birth', 'age', 'phone_no', 'email', 'gender', 'department', 'address', 'image']

        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'address': forms.Textarea(attrs={'style': 'height: 100px;'}),
        }
    
    def __init__(self, doctor=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        placeholders = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'date_of_birth': 'Date of Birth',
            'age': 10,
            'phone_no': 'Phone No',
            'email': 'abc@example.com',
            'address': 'Lorem Ipsum, Porem, CA, US',
        }
        
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'placeholder': placeholders.get(field),
            })


