from django.urls import path
from .views import EmployeeListVew, profile_employee

urlpatterns = [
    path('', EmployeeListVew.as_view(), name='employee'),
    path('<int:employee_id>/', profile_employee, name='profile_employee'),
]