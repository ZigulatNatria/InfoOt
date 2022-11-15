from django.urls import path
from .views import EmployeeListVew, profile_employee, medicine, certificate

urlpatterns = [
    path('', EmployeeListVew.as_view(), name='employee'),
    path('<int:employee_id>/', profile_employee, name='profile_employee'),
    path('medicine/<int:medicine_id>', medicine, name='medicine'),
    path('certificate/<int:employee_id>', certificate, name='certificate'),
]