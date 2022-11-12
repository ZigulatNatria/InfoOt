from django.shortcuts import render
from .models import Employee, Passport
from django.views.generic import ListView

# Create your views here.
class EmployeeListVew(ListView):
    model = Employee
    context_object_name = 'employee'
    template_name = 'index.html'
    queryset = Employee.objects.all()


def profile_employee(request, employee_id):
    employee = Employee.objects.all()
    passport = Passport.objects.all()
    current_profile = Employee.objects.get(pk=employee_id)
    context = {'employee': employee, 'passport': passport, 'current_profile': current_profile}
    return render(request, 'profile.html', context)