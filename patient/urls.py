from django.urls import path
from . import views

urlpatterns = [
    path('add-patient/', views.add_patient, name='add-patient'),
    path('edit-patient/<int:patient_id>', views.edit_patient_detail, name='edit-patient'),
    path('delete-patient/<int:patient_id>', views.delete_patient_detail, name='delete-patient'),
    path('patient-detail/<int:patient_id>', views.patient_detail, name='patient-detail'),
    path('search/', views.search_patients, name='search-patients'),
]